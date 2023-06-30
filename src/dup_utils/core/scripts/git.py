from __future__ import annotations

import re
import subprocess
import sys
from dataclasses import InitVar, dataclass
from datetime import date, datetime
from typing import List, Optional, Tuple

import click

from .utils import (
    Level as LV,
)
from .utils import (
    make_color,
)

cli_git: click.Command

PROJECT_IDS = ["SLO"]
BRANCH_TYPES = ["feature", "bug", "hot"]

REGEX_PROJECT_IDS = "|".join(PROJECT_IDS)
REGEX_BRANCH_TYPES = "|".join(BRANCH_TYPES)

# Should contain a capturing group to extract the reference:
REGEX_BRANCH = rf"^(?:{REGEX_BRANCH_TYPES})/((?:{REGEX_PROJECT_IDS})-[\d]{{1,5}})-[a-z]+(?:-[a-z]+)*$"

# Should contain a capturing group to extract the reference (note the dot at the end
# is optional as this script will add it automatically for us):
REGEX_MESSAGE = rf"^((?:{REGEX_PROJECT_IDS})-[\d]{{1,5}}): .+\.?$"

# No capturing group. Just checking for the bare minimum:
REGEX_BASIC_MESSAGE = "^.+$"

REGEX_COMMIT_MESSAGE = r"(?P<prefix>\w+)(?:\((?P<topic>\w+)\))?: (?P<header>.+)"

# These branch names are not validated with this same rules (permissions should be configured
# on the server if you want to prevent pushing to any of these):
BRANCH_EXCEPTIONS = [
    "feature",
    "dev",
    "main",
    "stable",
    "hotfix",  # for quickly fixing critical issues, usually with a temporary solution
    "bugfix",  # for fixing a bug
    "feature",  # for adding, removing or modifying a feature
    "test",  # for experimenting something which is not an issue
    "wip",  # for a work in progress"
]

COMMIT_PREFIX = (
    ("feat", "Features", ":dart:"),  # 🎯, 📋 :clipboard:
    ("fix", "Fix Bugs", ":gear:"),  # ⚙️, 🛠️ :hammer_and_wrench:
    ("docs", "Documents", ":page_facing_up:"),  # 📄, 📑 :bookmark_tabs:
    ("style", "Code Changes", ":art:"),  # 🎨, 📝 :memo:, ✒️ :black_nib:
    ("refactor", "Code Changes", ":construction:"),  # 🚧, 💬 :speech_balloon:
    ("perf", "Code Changes", ":chart_with_upwards_trend:"),  # 📈, ⌛ :hourglass:
    ("test", "Code Changes", ":test_tube:"),  # 🧪, ⚗️ :alembic:
    ("build", "Build & Workflow", ":toolbox:"),  # 🧰, 📦 :package:
    ("workflow", "Build & Workflow", ":rocket:"),  # 🚀, 🕹️ :joystick:
)

COMMIT_PREFIX_TYPE = (
    ("Features", ":clipboard:"),  # 📋
    ("Fix Bugs", ":hammer_and_wrench:"),  # 🛠️
    ("Documents", ":bookmark_tabs:"),  # 📑
    ("Code Changes", ":black_nib:"),  # ✒️
    ("Build & Workflow", ":package:"),  # 📦
)


@dataclass
class CommitMsg:
    content: InitVar[str]
    mtype: InitVar[str] = None

    def __post_init__(self, content: str, mtype: str):
        self.content: str = self.__prepare_msg(content)
        if not mtype:
            self.mtype: str = self.__gen_msg_type()

    def __gen_msg_type(self) -> str:
        prefix: str = self.content.split(":", maxsplit=1)[0]
        return next(
            (cp[1] for cp in COMMIT_PREFIX if prefix == cp[0]),
            "Code Changes",
        )

    @property
    def mtype_icon(self):
        return next(
            (cpt[1] for cpt in COMMIT_PREFIX_TYPE if cpt[0] == self.mtype),
            ":black_nib:",
        )

    @staticmethod
    def __prepare_msg(content: str) -> str:
        if re.match(r"^:\w+:", content):
            return content

        prefix, content = (
            content.split(":", maxsplit=1)
            if ":" in content
            else ("refactor", content)
        )
        icon: str = ""
        for cp in COMMIT_PREFIX:
            if prefix == cp[0]:
                icon = f"{cp[2]} "
        return f"{icon}{prefix}: {content.strip()}"


@dataclass(frozen=True)
class CommitLog:
    hash: str
    date: date
    msg: CommitMsg
    author: str

    def __str__(self) -> str:
        return "|".join(
            (
                self.hash,
                self.date.strftime("%Y-%m-%d"),
                self.msg.content,
                self.author,
            )
        )


def validate_for_warning(
    lines: List[str], multilines: bool = False
) -> List[str]:
    subject: str = lines[0]
    results: List[str] = []
    # RULE 02: Limit the subject line to 50 characters
    if len(subject) <= 20 or len(subject) > 50:
        results.append(
            "There should be between 21 and 50 characters in the commit title."
        )
    if len(lines) > 1 or multilines:
        if len(lines) <= 2:
            results.append(
                "There should at least 3 lines in your commit message."
            )

        # RULE 01: Separate subject from body with a blank line
        if lines[1].strip() != "":
            results.append(
                "There should be an empty line between "
                "the commit title and body."
            )
    return results


def validate_commit_msg(
    lines: List[str],
    multilines: bool = False,
) -> Tuple[List[str], LV]:
    if not lines:
        return (
            ["Please supply commit message without start with ``#``."],
            LV.ERROR,
        )

    rs = validate_for_warning(lines, multilines)
    if rs:
        return rs, LV.WARNING

    if multilines:
        has_story_id: bool = False
        for line in lines[1:]:
            # RULE 06: Wrap the body at 72 characters
            if len(line) > 72:
                rs.append("The commit body should wrap at 72 characters.")

            if line.startswith("["):
                has_story_id = True

        if not has_story_id:
            rs.append("Please add a Story ID in the commit message.")

    if not rs:
        return (
            ["The commit message has the required pattern."],
            LV.OK,
        )
    return rs, LV.WARNING


def get_branch_name() -> str:
    return (
        subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"])
        .decode("ascii")
        .strip()
    )


def get_latest_tag(default: bool = True) -> Optional[str]:
    try:
        return (
            subprocess.check_output(
                ["git", "describe", "--tags", "--abbrev=0"],
                stderr=subprocess.DEVNULL,
            )
            .decode("ascii")
            .strip()
        )
    except subprocess.CalledProcessError:
        if default:
            from ..__about__ import __version__

            return f"v{__version__}"
        return None


def get_commit_logs() -> List:
    """"""
    tag2head: str = (
        f"{tag}..HEAD" if (tag := get_latest_tag(default=False)) else "HEAD"
    )
    msgs = (
        subprocess.check_output(
            [
                "git",
                "log",
                tag2head,
                "--pretty=format:%h|%ad|%s%d|%an",
                "--date=short",
            ]
        )
        .decode("ascii")
        .strip()
        .split("\n")
    )
    for _ in msgs:
        _s = _.split("|")
        print(
            CommitLog(
                hash=_s[0],
                date=datetime.strptime(_s[1], "%Y-%m-%d"),
                msg=CommitMsg(content=_s[2]),
                author=_s[3],
            )
        )
    return msgs


def get_latest_commit(file: Optional[str] = None) -> List[str]:
    if not file:
        file = ".git/COMMIT_EDITMSG"
    with open(file, encoding="utf-8") as f_msg:
        raw_msg = f_msg.readlines()
    lines = [msg for msg in raw_msg if not msg.strip().startswith("#")]
    rss, level = validate_commit_msg(lines)
    if level == LV.OK:
        print(make_color(rss[0], level))
        with open(file, mode="w", encoding="utf-8") as file:
            file.write("\n".join(lines))
    else:
        for rs in rss:
            print(make_color(rs, level))
    return lines


def get_commit_message() -> List[str]:
    raw_msg = (
        subprocess.check_output(
            ["git", "log", "HEAD^..HEAD", "--pretty=format:%s"]
        )
        .decode("ascii")
        .strip()
        .split("\n")
    )
    lines = [msg for msg in raw_msg if not msg.strip().startswith("#")]
    print(validate_commit_msg(lines))
    return lines


def get_branch_ref(branch):
    match = re.findall(REGEX_BRANCH, branch)
    return match[0] if match and match[0] else None


@click.group(name="git")
def cli_git():
    """Git commands"""
    pass


@cli_git.command()
def bn():
    """Branch name"""
    sys.exit(get_branch_name())


@cli_git.command()
def ltn():
    """The Latest Tag name"""
    sys.exit(get_latest_tag())


@cli_git.command()
def cml():
    """Commit log from latest tag"""
    sys.exit("\n".join(get_commit_logs()))


@cli_git.command()
@click.option("-f", "--file", type=click.STRING, default=None)
@click.option("-l", "--latest", is_flag=True)
def cmm(latest: bool, file: Optional[str]):
    if latest or file:
        sys.exit("\n".join(get_latest_commit(file)))
    sys.exit("\n".join(get_commit_message()))


@cli_git.command()
def cmp():
    """Commit to the latest commit with same message"""
    subprocess.run(["git", "commit", "--amend", "--no-fix"])


if __name__ == "__main__":
    cli_git.main()
