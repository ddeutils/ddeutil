# Changelogs

## Latest Changes

## 0.4.4

### :black_nib: Code Changes

- :construction: refactored: remove debug decorator from this proj. (_2024-12-18_)
- :construction: refactored: remove cache module from this proj. (_2024-12-18_)
- :construction: refactored: ⬆ bump codecov/codecov-action from 4 to 5 (_2024-12-01_)
- :construction: refactored: ⬆ bump pypa/gh-action-pypi-publish from 1.11.0 to 1.12.2 (_2024-12-01_)
- :construction: refactored: 📦 bump types-python-dateutil from 2.9.0.20240906 to 2.9.0.20241003 (#58) (_2024-11-04_)
- :construction: refactored: ⬆ bump deadsnakes/action from 3.1.0 to 3.2.0 (_2024-11-01_)
- :construction: refactored: ⬆ bump pypa/gh-action-pypi-publish from 1.10.2 to 1.11.0 (_2024-11-01_)
- :construction: refactored: 📦 bump psutil from 6.0.0 to 6.1.0 (_2024-11-01_)

### :bug: Fix Bugs

- :gear: fixed: add ujson handler on base.convert module. (_2024-10-28_)

## 0.4.3

### :black_nib: Code Changes

- :construction: refactored: list module to __all__ at the base module. (_2024-10-16_)

### :card_file_box: Documents

- :page_facing_up: docs: update usages content on readme. (_2024-10-16_)
- :page_facing_up: docs: update docs-str on the convert module. (_2024-10-16_)
- :page_facing_up: docs: update desc of features on readme. (_2024-10-07_)
- :page_facing_up: docs: update readme for optional deps. (_2024-10-07_)

### :bug: Fix Bugs

- :gear: fixed: add import direct to function from __base. (_2024-10-07_)

## 0.4.2

### :black_nib: Code Changes

- :test_tube: tests: add testcases for cover coverage report 100%. (_2024-10-07_)
- :art: styled: change in-condition from set to tuple. (_2024-10-05_)
- :test_tube: tests: add testcase for increase coverage report. (_2024-10-05_)

### :card_file_box: Documents

- :page_facing_up: docs: update readme. (_2024-10-06_)
- :page_facing_up: docs: update readme for new funcs and objs. (_2024-10-05_)

### :bug: Fix Bugs

- :gear: fixed: remove pre-commit call pytest on commit stage. (_2024-10-05_)

### :package: Build & Workflow

- :toolbox: build: add coverage workflow. (_2024-10-06_)
- :toolbox: build: change version of cache file. (_2024-10-05_)

## 0.4.1

### :sparkles: Features

- :dart: feat: add monitoring thread and getdot support ? syntax. (_2024-10-05_)

### :black_nib: Code Changes

- :test_tube: tests: add testcase for dtutil module. (_2024-10-05_)
- :test_tube: tests: add hasdot and setdot testcases. (_2024-10-05_)
- :construction: refactored: ⬆ bump pypa/gh-action-pypi-publish from 1.10.0 to 1.10.2 (_2024-10-01_)
- :construction: refactored: 📦 bump types-python-dateutil from 2.9.0.20240821 to 2.9.0.20240906 (_2024-10-01_)
- :construction: refactored: change import of this package. (_2024-09-26_)

### :card_file_box: Documents

- :page_facing_up: docs: update duplicate info on readme. (_2024-09-26_)
- :page_facing_up: docs: list all functions that provide from this package. (_2024-09-26_)

### :package: Build & Workflow

- :toolbox: build: add python 3.13 with nogil in test workflow. (_2024-10-05_)

### :postbox: Dependencies

- :pushpin: deps: add psutil==6.0.0 deps on all option. (_2024-10-05_)

## 0.4.0

### :sparkles: Features

- :dart: feat: change name of property caching func and move random string func loc. (_2024-09-26_)

### :black_nib: Code Changes

- :test_tube: tests: change name of pytest on pre-commit hook local. (_2024-09-22_)

### :card_file_box: Documents

- :page_facing_up: docs: update feature table on readme. (_2024-09-26_)
- :page_facing_up: docs: update readme for notice about optional deps. (_2024-09-26_)
- :page_facing_up: docs: update readme and create docs folder for mkdocs. (_2024-09-22_)

### :postbox: Dependencies

- :pushpin: deps: move all deps to optional deps. (_2024-09-26_)
- :pushpin: deps: remove tzdata from project dependency. (_2024-09-26_)

## 0.3.8

### :bug: Fix Bugs

- :gear: fixed: add hash for list and set type in freeze_args func. (_2024-09-13_)

### :package: Build & Workflow

- :toolbox: build: add support for python version 3.13. (_2024-09-13_)

## 0.3.7

### :sparkles: Features

- :dart: feat: add datetime utils function. (_2024-09-13_)

### :black_nib: Code Changes

- :construction: refactored: ⬆ bump pypa/gh-action-pypi-publish from 1.9.0 to 1.10.0 (_2024-09-01_)

### :card_file_box: Documents

- :page_facing_up: docs: update readme and remove license topic. (_2024-08-26_)

### :bug: Fix Bugs

- :gear: fixed: freeze_args does not freeze all items. (_2024-09-13_)

## 0.3.6

### :sparkles: Features

- :dart: feat: add handler number of digit value in hash_str function. (_2024-08-26_)
- :dart: feat: add year mode on dtutils module. (_2024-08-26_)

### :black_nib: Code Changes

- :construction: refactored: ⬆ bump pypa/gh-action-pypi-publish from 1.8.14 to 1.9.0 (_2024-07-01_)
- :construction: refactored: 📦 bump ujson from 5.9.0 to 5.10.0 (#51) (_2024-06-03_)

### :card_file_box: Documents

- :page_facing_up: docs: update readme file for more example. (_2024-06-04_)

### :postbox: Dependencies

- :pushpin: deps: update version of types-python-dateutil to 2.9.0.20240821. (_2024-08-26_)

## 0.3.5

### :sparkles: Features

- :dart: feat: add lazy function for lazy import string. (_2024-05-26_)

### :black_nib: Code Changes

- :test_tube: tests: add testcase for increase coverage on hash and checker. (_2024-05-19_)
- :construction: refactored: remove base dir and add doc-str. (_2024-05-18_)
- :art: style: add type hint for time decoratored. (_2024-05-16_)

### :bug: Fix Bugs

- :gear: fixed: change time.time to monotonic instead. (_2024-05-19_)
- :gear: fixed: import lose function from __base. (_2024-05-13_)

### :package: Build & Workflow

- :toolbox: build: add black that was removed from my mistake. (_2024-05-18_)

## 0.3.4

### :black_nib: Code Changes

- :construction: refactored: change str docs and add __types file for make base type. (_2024-05-13_)
- :construction: refactored: change str docs and add __types file for make base type. (_2024-05-13_)
- :construction: refactored: rewrite getter args and change type hint. (_2024-05-05_)

### :card_file_box: Documents

- :page_facing_up: docs: update readme and remove deleted topic. (_2024-05-05_)

### :bug: Fix Bugs

- :gear: fixed: mrge branch that conflict with local. (_2024-05-13_)

### :postbox: Dependencies

- :pushpin: deps: remove optional dependencies from pyproject. (_2024-05-13_)

## 0.3.3

### :bug: Fix Bugs

- :gear: fixed: remove test import on tests workflow. (_2024-05-05_)

### :package: Build & Workflow

- :toolbox: build: fixed find files on setuptools backend. (_2024-05-05_)
- :toolbox: build: add test import workflow. (_2024-05-05_)

### :postbox: Dependencies

- :pushpin: deps: update pre-commit hook deps. (_2024-05-05_)

## 0.3.2

### :sparkles: Features

- :dart: feat: add type hint for decorator functions. (_2024-04-29_)

### :black_nib: Code Changes

- :construction: refactored: 📦 bump pytest from 8.1.1 to 8.2.0 (#49) (_2024-05-01_)
- :construction: refactored: 📦 bump clishelf from 0.2.0 to 0.2.1 (_2024-05-01_)

### :bug: Fix Bugs

- :gear: fixed: merge branch from remote into local. (_2024-05-05_)

### :package: Build & Workflow

- :toolbox: build: split step of publish workflow for each environment. (_2024-05-05_)

## 0.3.1

### :black_nib: Code Changes

- :construction: refactored: remove not necessary code from this package. (_2024-04-28_)
- :construction: refactored: ⬆ bump pypa/gh-action-pypi-publish from 1.8.12 to 1.8.14 (_2024-04-01_)
- :construction: refactored: 📦 bump types-python-dateutil from 2.8.19.20240311 to 2.9.0.20240316 (_2024-04-01_)
- :construction: refactored: 📦 bump python-dateutil from 2.9.0 to 2.9.0.post0 (_2024-04-01_)
- :construction: refactored: remove dynamic zoneinfo that support for py38. (_2024-03-12_)

### :card_file_box: Documents

- :page_facing_up: docs: remove example docs from readme file. (_2024-04-28_)
- :page_facing_up: docs: update project urls on pyproject file. (_2024-03-11_)

## 0.3.0

> [!NOTE]
> This version start support python version >= 3.9.13.

### :sparkles: Features

- :dart: feat: upgrade python version from 3.8 to 3.9. (_2024-03-11_)

## 0.2.4

### :black_nib: Code Changes

- :construction: refactored: 📦 update python-dateutil requirement from <3.0.0,==2.8.2 to ==2.9.0 (#44) (_2024-03-03_)
- :construction: refactored: ⬆ bump pypa/gh-action-pypi-publish from 1.8.11 to 1.8.12 (_2024-03-01_)
- :construction: refactored: 📦 bump tzdata from 2023.4 to 2024.1 (_2024-03-01_)
- :construction: refactored: 📦 bump clishelf from 0.1.2 to 0.1.8 (_2024-03-01_)

### :card_file_box: Documents

- :page_facing_up: docs: update README file for more information. (_2024-03-03_)
- :page_facing_up: docs: update example code to README. (_2024-01-29_)

### :postbox: Dependencies

- :pushpin: deps: update dependencies and workflow deps. (_2024-03-03_)

## 0.2.3

> [!NOTE]
> Change the Repository location from Personal to Organization, `ddeutils`.

### Code Changes

- :construction: refactored: remove vendor from this repo and move to ddeutil-dataframe. (_2024-01-28_)
- :construction: refactored: 📦 bump clishelf from 0.1.1 to 0.1.2 (#41) (_2024-01-28_)
- :construction: refactored: 📦 bump types-python-dateutil from 2.8.19.14 to 2.8.19.20240106 (_2024-01-28_)
- :construction: refactored: ⬆ bump actions/cache from 3 to 4 (_2024-01-28_)

### Fix Bugs

- :gear: fixed: remove vendor path on pyproject config. (_2024-01-29_)
- :gear: fixed: remove bumpversion config file from local. (_2024-01-28_)

## 0.2.2

### Features

- :dart: feat: remove some funcs that does not use. (_2024-01-24_)

### Documents

- :page_facing_up: docs: update README that remove some func. (_2024-01-24_)
- :page_facing_up: docs: update README file. (_2024-01-22_)

## 0.2.1

### Features

- :dart: feat: add some decorator funcs from python blog. (_2023-10-05_)

### Code Changes

- :construction: refactored: remove parallel and example of thread. (_2024-01-14_)
- :construction: refactored: merge filtering and randomly. (_2024-01-14_)
- :construction: refactored: ⬆ bump actions/setup-python from 4 to 5 (_2024-01-01_)
- :construction: refactored: 📦 bump clishelf from 0.1.0 to 0.1.1 (_2024-01-01_)
- :construction: refactored: 📦 bump tzdata from 2023.3 to 2023.4 (_2024-01-01_)
- :construction: refactored: 📦 update ujson requirement from <6.0.0,==5.8.0 to ==5.9.0 (_2024-01-01_)
- :construction: refactored: ⬆ bump pypa/gh-action-pypi-publish from 1.8.10 to 1.8.11 (_2023-12-01_)
- :construction: refactored: ⬆ bump clishelf from 0.0.4 to 0.1.0 (_2023-11-01_)
- :art: style: add prefix on pre-commit ci hook and skip local test. (_2023-09-12_)
- :construction: refactored: [pre-commit.ci] auto fixes from pre-commit.com hooks (_2023-09-11_)
- :construction: refactored: ⬆ bump actions/checkout from 3 to 4 (_2023-09-11_)
- :construction: refactored: remove contribute file from this project. (_2023-09-09_)

### Documents

- :page_facing_up: docs: update README for list all of features. (_2024-01-14_)
- :page_facing_up: docs: remove cli from README. (_2023-09-08_)

### Fix Bugs

- :gear: fixed: change config key of clishelf. (_2024-01-14_)

### Build & Workflow

- :toolbox: build: change frequency of dependabot from weekly to monthly. (_2023-11-22_)
- :toolbox: build: update deps version on pyproject. (_2023-10-12_)
- :toolbox: build: change hook id on pre-commit config file. (_2023-09-12_)

## 0.2.0

### Code Changes

- reafactored: remove cli feature from this project. (_2023-09-08_)
- :test_tube: test: upgrade pre-commit hooks. (_2023-09-07_)

### Documents

- :page_facing_up: docs: update README and change url of source code on pyproject. (_2023-09-07_)

## 0.1.0

### Features

- :dart: feat: init features of git and version cli. (_2023-09-05_)

### Code Changes

- :construction: refactored: change package name from dup-utils to ddeutil on PyPI. (_2023-09-07_)

### Documents

- :page_facing_up: docs: update source code url to GitHub page. (_2023-09-06_)

### Fix Bugs

- :fire: hotfix: add loss function from base init file (_2023-08-28_)

## 0.0.5.post0

### Code Changes

- :art: style: remove src prefix in import any modules. (_2023-08-28_)

### Fix Bugs

- :fire: hotfix: adjust reset commit on bump cli command. (_2023-08-27_)

## 0.0.5

### Features

- :dart: feat: add filtering and pathutils features. (_2023-08-26_)
- :dart: feat: add coverage cli command. (_2023-08-25_)

### Fix Bugs

- :gear: fixed: fix import internal module. (_2023-08-26_)

## 0.0.4

### Code Changes

- :test_tube: test: add more initial test cases. (_2023-08-22_)
- :art: style: change getter style of private attributes or methods. (_2023-08-22_)
- :construction: refactored: rename core function and remove queues. (_2023-08-22_)
- :construction: refactor: ⬆ bump pypa/gh-action-pypi-publish from 1.8.6 to 1.8.10 (#11) (_2023-08-20_)
- :package: Create dependabot.yml (_2023-08-20_)

### Fix Bugs

- :gear: fixed: git in bump cli does not add config file after create. (_2023-08-24_)
- :fire: hotfix: fix tomli dependency package. (_2023-08-22_)

## 0.0.3

### Features

- :dart: feat: add option for ignore generate changelog before bump version. (_2023-08-15_)

### Code Changes

- :bookmark: Bump up to version 0.0.2.post1 -> 0.0.3. (_2023-08-16_)
- :test_tube: test: add test cases for base feature (_2023-08-15_)
- :construction: refactored: split merge and split features to 2 files (_2023-08-07_)

### Fix Bugs

- :gear: fixed: fix import module that was changed name of package (_2023-08-15_)
- :gear: fix: change delete command to force delete (_2023-07-11_)

## 0.0.2.post1

### Features

- :dart: feat: add force flag for commit-revert command (_2023-07-11_)

### Code Changes

- :construction: refactored: add commit subprocess instead merge2latest func (_2023-07-11_)

### Fix Bugs

- :gear: fix: change decode of subprocess that use ascii to stdout.encoding (#8) (_2023-07-11_)

## 0.0.2

### Features

- :dart: feat: create cli script for git and version (#5) (_2023-07-08_)

### Code Changes

- :construction: refactor: change function name and generate group logs (#6) (_2023-07-09_)

## 0.0.1

### Features

- :dart: feat: add bump2version for change version release (HEAD -> feature) (_2023-07-01_)
- :dart: feat: add edit commit message and re-write message (_2023-06-30_)
- :dart: feat: add validate commit message in git cli (origin/feature) (_2023-06-30_)
- :dart: feat: add cli scripts with git commands (_2023-06-28_)
- :dart: feat: add cache package to base (_2023-06-26_)
- :dart: feat: add hash to base utility package (_2023-06-23_)
- :dart: feat: rename base function and change code format (_2023-06-23_)
- :dart: feat: add convert fumction for str to int (_2023-06-23_)
- :dart: feat: resturcture for core package only (_2023-06-23_)
- :dart: feat: restructure project for supported the namespace sub-package (_2023-06-22_)
- :dart: feat: initial first module for dbutil (_2023-06-21_)
- :dart: feat: add initial files for this package (_2023-06-20_)

### Code Changes

- add: utils features (_2023-06-22_)
- :construction: refactor: Initial commit (_2023-06-20_)

### Documents

- :page_facing_up: docs: prepare pyproject.toml (_2023-06-21_)

### Build & Workflow

- :rocket: workflow: edit publish yaml file for workflow_dispatch (_2023-06-26_)
- :rocket: workflow: add test workflow for push and pull_request (_2023-06-23_)

## 0.0.0

- :octocat: Initial project on GitHub
