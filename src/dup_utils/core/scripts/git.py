from __future__ import annotations

import re
import subprocess
import sys
from typing import List, Optional

import click

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
]

COMMIT_PREFIX = (
    ("feat", ":dart:"),  # 🎯, 📋 :clipboard:
    ("fix", ":gear:"),  # ⚙️, 🛠️ :hammer_and_wrench:
    ("docs", ":page_facing_up:"),  # 📄, 📑 :bookmark_tabs:
    ("style", ":art:"),  # 🎨, 📝 :memo:, ✒️ :black_nib:
    ("refactor", ":construction:"),  # 🚧, 💬 :speech_balloon:
    ("perf", ":chart_with_upwards_trend:"),  # 📈, ⌛ :hourglass:
    ("test", ":test_tube:"),  # 🧪, ⚗️ :alembic:
    ("build", ":toolbox:"),  # 🧰, 📦 :package:
    ("workflow", ":rocket:"),  # 🚀, 🕹️ :joystick:
)


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
    return (
        subprocess.check_output(
            [
                "git",
                "log",
                tag2head,
                "--pretty=format:%h|%ad|%s%d|[%an]",
                "--date=short",
            ]
        )
        .decode("ascii")
        .strip()
        .split("\n")
    )


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
def cmp():
    """Commit to the latest commit with same message"""
    subprocess.run(["git", "commit", "--amend", "--no-fix"])


if __name__ == "__main__":
    cli_git.main()
