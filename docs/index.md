# Core Data Utility

The **Core Data Utility** package implements the data utility functions and objects
that was created on sub-package namespace, `ddeutil`, design for independent
installation.

I make this package able to extend with any sub-extension with this namespace.
So, this namespace able to scale-out the requirement with folder level design.
You can add any custom features and import it by `import ddeutil.{extension}`.

!!! note

    This package provide the Base Utility functions and objects for any sub-namespace
    package that use for data function or application.

## :round_pushpin: Installation

```shell
pip install -U ddeutil
```

## :dart: Features

This Core package will implement all of reusable functions and objects that does
not re-create again because it is basic code but has a lot of coding.

```text
core
  - base
    - cache
    - checker
    - convert
    - hash
    - merge
    - sorting
    - splitter
  - decorator
  - dtutils
  - randomly
```
