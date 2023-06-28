from pathlib import Path


def pwd() -> Path:
    return Path(".")


def ls(path: str):
    yield from pwd().glob(path)


def readline(path: str):
    file = pwd() / Path(path)
    return file.read_text(encoding="utf-8")
