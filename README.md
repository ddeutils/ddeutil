# Core Data Utility

[![test](https://github.com/korawica/ddeutil/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/korawica/ddeutil/actions/workflows/tests.yml)
[![pypi version](https://img.shields.io/pypi/v/ddeutil)](https://pypi.org/project/ddeutil/)
[![python support version](https://img.shields.io/pypi/pyversions/ddeutil)](https://pypi.org/project/ddeutil/)
[![python support version](https://img.shields.io/pypi/pyversions/ddeutil)](https://pypi.org/project/ddeutil/)
[![size](https://img.shields.io/github/languages/code-size/korawica/ddeutil)](https://github.com/korawica/ddeutil)
[![code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

The **Core Data Utility** package implements the data utility functions and objects
that was created on sub-package namespace, `ddeutil`, design for independent
installation.

I make this package able to extend with any sub-extension with this namespace.
So, this namespace able to scale-out the requirement with folder level design.
You can add any custom features and import it by `import ddeutil.{extension}`.

> [!NOTE]
> This package provide the Base Utility functions and objects for any sub-namespace
> package that use for data function or application.

## :round_pushpin: Installation

```shell
pip install -U ddeutil
```

**Python version supported**:

| Python Version | Installation                        | Support Fixed Bug  |
|----------------|-------------------------------------|--------------------|
| `>=3.9,<3.14`  | `pip install -U ddeutil`            | :heavy_check_mark: |

> [!NOTE]
> If you want to install all optional dependencies for this package, you can use
> `pip install -U ddeutil[all]`. I will install `ujson` and `python-dateutil`
> packages for some functions in this project such as `hash.checksum`, 
> `dtutils.next_date_with_freq`.

## :dart: Features

This Core package will implement all of reusable functions and objects that does
not re-create again because it is basic code but has a lot of coding.

| Module        | Function            | Import Syntax                                   | Description                                                                                                     |
|---------------|---------------------|-------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| base          | `isinstance_check`  | `from <package> import isinstance_check`        |                                                                                                                 |
| base.cache    | `memorize`          | `from <package>.cache import memorize`          | Return a cachable function that keep all arguments and pass to string type for keeping it in the caching key.   |
|               | `property_memorize` | `from <package>.cache import property_memorize` |                                                                                                                 |
|               | `clear_cache`       | `from <package>.cache import clear_cache`       |                                                                                                                 |
| base.checker  | `can_int`           | `from <package>.cache import can_int`           |                                                                                                                 |
|               | `is_int`            | `from <package>.cache import is_int`            |                                                                                                                 |
| base.convert  |                     |                                                 |                                                                                                                 |
| base.hash     |                     |                                                 |                                                                                                                 |
| base.merge    |                     |                                                 |                                                                                                                 |
| base.sorting  |                     |                                                 |                                                                                                                 |
| base.splitter |                     |                                                 |                                                                                                                 |
| decorator     |                     |                                                 |                                                                                                                 |
| dtutils       |                     |                                                 |                                                                                                                 |
| threader      |                     |                                                 |                                                                                                                 |


## :beers: Usages

### OnlyOne

```python
from ddeutil.core import onlyone

assert 'a' == onlyone(['a', 'b'], ['a', 'b', 'c'])
assert 'c' == onlyone(('a', 'b'), ['c', 'e', 'f'])
assert onlyone(['a', 'b'], ['c', 'e', 'f'], default=False) is None
```

### Instance Check

```python
from ddeutil.core import isinstance_check
from typing import Union, Optional

assert isinstance_check("s", str)
assert isinstance_check(["s"], list[str])
assert isinstance_check(("s", "t"), tuple[str, ...])
assert not isinstance_check(("s", "t"), tuple[str])
assert isinstance_check({"s": 1, "d": "r"}, dict[str, Union[int, str]])
assert isinstance_check("s", Optional[str])
assert isinstance_check(1, Optional[Union[str, int]])
assert not isinstance_check("s", list[str])
```
