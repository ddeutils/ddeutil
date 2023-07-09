# Contributing

**Table of Contents**:

- [Getting Installed](#getting-installed)
- [Test Installation](#test-installation)
- [Release Code](#release-code)

## Getting Installed

```shell
git clone https://github.com/korawica/dup-utils.git
```

> **Note**: \
> If you want to set new user and email before push your edited code,
> ```shell
> git config --local user.name "Korawich Anuttra"
> git config --local user.email "korawich.anu@gmail.com"
> git config --local credential.helper ""
> ```
> If you commit with old user and email completely, you can change by:
> ```shell
> git commit --amend --no-edit \
>   --author="Korawich Anuttra <korawich.anu@gmail.com>"
> ```

```shell
python -m pip install --upgrade pip
python -m venv venv
./env/Scripts/activate
```

> **Note**: \
> For create performance, you can use `virtualenv` instead of build-in `venv`.

```shell
(venv) $ pip install -e ".[test,dev]" --no-cache
(venv) $ pip uninstall dup-utils
```

## Test Installation

```shell
(venv) $ pip install --index-url https://test.pypi.org/simple/ \
  --extra-index-url https://pypi.org/simple/ \
  --no-cache \
  "dup-utils[test,dev]"
(venv) $ pytest -v
```

```shell
(venv) $ git add . ; git commit --amend --no-edit
```

## Release Code

```shell
bump2version patch
```

> **Note**: \
> `git restore .`
