import click

BUMP_VERSION = (("bump", ":bookmark:"),)  # 🔖 :bookmark:


@click.group(name="version")
def cli_git():
    """Git commands"""
    pass
