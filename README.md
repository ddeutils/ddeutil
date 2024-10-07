# Core Data Utility

[![test](https://github.com/korawica/ddeutil/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/korawica/ddeutil/actions/workflows/tests.yml)
[![codecov](https://codecov.io/gh/ddeutils/ddeutil/graph/badge.svg?token=G3XGBSRKA6)](https://codecov.io/gh/ddeutils/ddeutil)
[![pypi version](https://img.shields.io/pypi/v/ddeutil)](https://pypi.org/project/ddeutil/)
[![python support version](https://img.shields.io/pypi/pyversions/ddeutil)](https://pypi.org/project/ddeutil/)
[![size](https://img.shields.io/github/languages/code-size/korawica/ddeutil)](https://github.com/korawica/ddeutil)
[![code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![type check: mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

The **Core Data utility** package implements the data utility functions and objects
that was created on sub-package namespace, `ddeutil`, design for independent
installation.

I make this package able to extend with any sub-extension with this namespace.
So, this namespace able to scale-out the requirement with folder level design.
You can add any custom features and import it by `import ddeutil.{extension}`.

> [!NOTE]
> This package provide the base utility functions and objects for any sub-namespace
> package.

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
> `pip install -U ddeutil[all]`. For optional dependencies that use on this
> package, it will list on below table;
> 
> | Optional deps     | Module                                                  |
> |-------------------|---------------------------------------------------------|
> | `ujson`           | `hash.checksum`                                         |
> | `python-dateutil` | `dtutils.next_date_with_freq`, `dtutils.calc_data_freq` | 
> | `psutil`          | `threader.MonitorThread`.                               |

## :dart: Features

This core data package will implement all of utility functions and objects that
does not re-create again because it is basic code but has a lot of using require.

| Module          |         Name          | Description                                                                                                            | Remark       |
|:----------------|:---------------------:|------------------------------------------------------------------------------------------------------------------------|--------------|
| base            |  `isinstance_check`   | Return True if a data is instance of the respect instance.                                                             |              |
|                 |    `import_string`    | Import a dotted module path and return the attribute/class designated by the last name in the path.                    |              |
|                 |        `lazy`         | Lazy use import_string function that wrapped with partial function.                                                    |              |
|                 |      `round_up`       | Round up the number with decimals precision size.                                                                      |              |
|                 |     `remove_pad`      | Remove zero padding of zero prefix string.                                                                             |              |
|                 |        `first`        | Returns the first item in the `iterable` that satisfies the `condition`.                                               |              |
|                 |       `onlyone`       | Get only one element from check list that exists in match list.                                                        |              |
|                 |       `hasdot`        | Return True value if dot searching exists in content data.                                                             |              |
|                 |       `getdot`        | Return the value if dot searching exists in content data.                                                              |              |
|                 |       `setdot`        | Set the value if dot searching exists in content data.                                                                 |              |
|                 |     `filter_dict`     | Filter dict value with excluded and included collections.                                                              |              |
|                 |     `random_str`      | Random string from uppercase ASCII and number 0-9.                                                                     | no coverage  |
|                 |      `coalesce`       | Coalesce function that is a just naming define function.                                                               | no coverage  |
| base.cache      |      `memorize`       | Return a cachable function that keep all arguments and pass to string type for keeping it in the caching key.          |              |
|                 |  `property_memorize`  | Return a property attribute for new-style classes that only calls its getter on the first access.                      |              |
|                 |     `clear_cache`     | Clear cache or the another word is delete caching attribute value that implement cache with target attribute property. |              |
| base.checker    |       `can_int`       |                                                                                                                        |              |
|                 |       `is_int`        |                                                                                                                        |              |
| base.convert    |      `must_bool`      |                                                                                                                        |              |
|                 |      `must_list`      |                                                                                                                        |              |
|                 |       `str2any`       |                                                                                                                        |              |
|                 |      `str2args`       |                                                                                                                        |              |
|                 |      `str2bool`       |                                                                                                                        |              |
|                 |      `str2dict`       |                                                                                                                        |              |
|                 |    `str2int_float`    |                                                                                                                        |              |
|                 |      `str2list`       |                                                                                                                        |              |
| base.hash       |      `checksum`       |                                                                                                                        |              |
|                 |       `freeze`        |                                                                                                                        |              |
|                 |     `freeze_args`     |                                                                                                                        |              |
|                 |      `hash_all`       |                                                                                                                        |              |
|                 |      `hash_pwd`       |                                                                                                                        |              |
|                 |      `hash_str`       |                                                                                                                        |              |
|                 |      `same_pwd`       |                                                                                                                        |              |
|                 |      `tokenize`       |                                                                                                                        |              |
| base.merge      |     `merge_dict`      |                                                                                                                        |              |
|                 |  `merge_dict_value`   |                                                                                                                        |              |
|                 |  `merge_dict_values`  |                                                                                                                        |              |
|                 |     `merge_list`      |                                                                                                                        |              |
|                 |    `merge_values`     |                                                                                                                        |              |
|                 |      `zip_equal`      |                                                                                                                        |              |
| base.sorting    |       `ordered`       |                                                                                                                        |              |
|                 |    `sort_priority`    |                                                                                                                        |              |
| base.splitter   |       `isplit`        |                                                                                                                        |              |
|                 |     `must_rsplit`     |                                                                                                                        |              |
|                 |     `must_split`      |                                                                                                                        |              |
| decorator       |      `deepcopy`       |                                                                                                                        |              |
|                 |    `deepcopy_args`    |                                                                                                                        |              |
|                 |       `timing`        |                                                                                                                        |              |
|                 |     `timing_open`     |                                                                                                                        |              |
|                 |        `debug`        |                                                                                                                        |              |
|                 |        `retry`        |                                                                                                                        |              |
|                 |       `profile`       | Profile the current memory and cpu usage while wrapped function running.                                               |              |
| dtutils         |    `replace_date`     | Replace datetime matrix that less than an input mode to origin value.                                                  |              |
|                 |      `next_date`      | Return the next date with specific unit mode.                                                                          |              |
|                 |   `closest_quarter`   | Return closest quarter datetime of an input datetime.                                                                  |              |
|                 |      `last_dom`       | Get the latest day of month that relate with an input datetime value.                                                  |              |
|                 |      `last_doq`       | Get the latest day of quarter that relate with an input datetime value.                                                |              |
|                 |   `next_date_freq`    |                                                                                                                        |              |
|                 |   `calc_data_freq`    |                                                                                                                        |              |
| threader        |  `ThreadWithControl`  | Threading object that can control maximum background agent and result after complete.                                  |              |
|                 |    `MonitorThread`    | Monitoring threading object that log the current memory and cpu usage.                                                 |              |

## :beers: Usages

I will show some usage example of function in this package. If you want to use
complex or adjust some parameter, please see doc-string or real source code
(I think it do not complex and you can see how that function work).

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
