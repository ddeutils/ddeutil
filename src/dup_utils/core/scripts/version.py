from __future__ import annotations

import os
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path
from typing import Dict, List

import click

BUMP_VERSION = (("bump", ":bookmark:"),)  # 🔖 :bookmark:

BUMP_REGEX = (
    r"(?P<major>\d+)\.(?P<minor>\d+)\.(?P<patch>\d+)"
    r"(\.(?P<prekind>a|alpha|b|beta|d|dev|rc)(?P<pre>\d+))?"
    r"(\.(?P<postkind>post)(?P<post>\d+))?"
)

BUMP_VERSION_CONFIG = r"""[bumpversion]
current_version = {version}
commit = True
tag = False
parse = ^
    (?P<major>\d+)\.(?P<minor>\d+)\.(?P<patch>\d+)
    (\.(?P<prekind>a|alpha|b|beta|d|dev|rc)(?P<pre>\d+))?
    (\.(?P<postkind>post)(?P<post>\d+))?
serialize =
    {{major}}.{{minor}}.{{patch}}.{{prekind}}{{pre}}.{{postkind}}{{post}}
    {{major}}.{{minor}}.{{patch}}.{{prekind}}{{pre}}
    {{major}}.{{minor}}.{{patch}}.{{postkind}}{{post}}
    {{major}}.{{minor}}.{{patch}}
message = :bookmark: Bump up to version {{current_version}} -> {{new_version}}.

[bumpversion:part:prekind]
optional_value = _
values =
    _
    dev
    a
    b
    rc

[bumpversion:part:postkind]
optional_value = _
values =
    _
    post

[bumpversion:file:{file}]

[bumpversion:file:{changelog}]
search = ## Latest Changes
replace = ## {{new_version}}
"""

cli_vs: click.Command


def generate_group_commit_log() -> Dict[str, List[tuple]]:
    """Generate Group of the Commit Logs"""
    from .git import get_commit_logs

    group_logs: Dict[str, List[tuple]] = defaultdict(list)
    for _ in get_commit_logs():
        group_logs[_.msg.mtype].append((_.date, _.msg.content, _.author))
    return {
        k: sorted(v, key=lambda x: x[0], reverse=True)
        for k, v in group_logs.items()
    }


def writer_changelog():
    group_logs: Dict[str, List[tuple]] = generate_group_commit_log()

    with Path("CHANGELOG.md").open(encoding="utf-8") as f_changes:
        changes = f_changes.read().splitlines()

    writer = Path("CHANGELOG.md").open(mode="w", encoding="utf-8", newline="")
    skip_line: bool = True
    written: bool = False
    for line in changes:
        if line.startswith("## Latest Changes"):
            skip_line = False

        if re.match(rf"## {BUMP_REGEX}", line):
            if not written:
                writer.write(f"## Latest Changes{os.linesep}{os.linesep}")
            skip_line = True

        if skip_line:
            writer.write(line + os.linesep)
            continue
        elif written:
            continue
        else:
            from .git import COMMIT_PREFIX_TYPE

            linesep = os.linesep
            if any(cpt[0] in group_logs for cpt in COMMIT_PREFIX_TYPE):
                linesep = f"{os.linesep}{os.linesep}"

            writer.write(f"## Latest Changes{linesep}")

            for cpt in COMMIT_PREFIX_TYPE:
                if cpt_exist := group_logs.get(cpt[0], []):
                    writer.write(f"### {cpt[0]}{os.linesep}{os.linesep}")
                    for cm in cpt_exist:
                        writer.write(
                            f"- {cm[1]} (_{cm[0]:%Y-%m-%d}_)" f"{os.linesep}"
                        )
                    writer.write(os.linesep)
            written = True
    writer.close()


def generate_version(
    action: str,
    file: str,
    changelog: str,
    dry_run: bool = False,
):
    from .git import merge2latest_commit

    with Path(".bumpversion.cfg").open(mode="w", encoding="utf-8") as f_bump:
        f_bump.write(
            BUMP_VERSION_CONFIG.format(
                file=file,
                version=current_version(file),
                changelog=changelog,
            )
        )
    writer_changelog()
    merge2latest_commit(no_verify=True)
    subprocess.run(
        [
            "bump2version",
            action,
            "--commit-args=--no-verify",
        ]
        + (["--list", "--dry-run"] if dry_run else [])
    )
    writer_changelog()
    merge2latest_commit(no_verify=True)

    # Path(".bumpversion.cfg").unlink(missing_ok=False)
    return 0


def current_version(file: str) -> str:
    with Path(file).open(encoding="utf-8") as f:
        if search := re.search(BUMP_REGEX, f.read()):
            return search[0]
    raise NotImplementedError(f"{file} does not implement version value.")


@click.group(name="vs")
def cli_vs():
    """Version commands"""
    pass


@cli_vs.command()
def mcl():
    """Make Changelogs file"""
    writer_changelog()
    sys.exit(0)


@cli_vs.command()
@click.option("-f", "--file", type=click.Path(exists=True))
def current(file: str):
    sys.exit(current_version(file))


@cli_vs.command()
@click.argument("action", type=click.STRING)
@click.option("-f", "--file", type=click.Path(exists=True))
@click.option("-c", "--changelog", type=click.Path(exists=True))
@click.option("--dry-run", is_flag=True)
def bump(action: str, file: str, changelog: str, dry_run: bool):
    if not file:
        file = r".\src\dup_utils\core\__about__.py"
    if not changelog:
        changelog = "CHANGELOG.md"
    sys.exit(generate_version(action, file, changelog, dry_run))


if __name__ == "__main__":
    cli_vs.main()
