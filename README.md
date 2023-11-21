[<img src="http://beeware.org/static/images/defaultlogo.png" width="72px" alt="Generic BeeWare Logo">](https://beeware.org/)

# setuptools_dynamic_dependencies

[![Python Versions](https://img.shields.io/pypi/pyversions/setuptools_dynamic_dependencies.svg)](https://pypi.python.org/pypi/setuptools_dynamic_dependencies)
[![PyPI Version](https://img.shields.io/pypi/v/setuptools_dynamic_dependencies.svg)](https://pypi.python.org/pypi/setuptools_dynamic_dependencies)
[![Maturity](https://img.shields.io/pypi/status/setuptools_dynamic_dependencies.svg)](https://pypi.python.org/pypi/setuptools_dynamic_dependencies)
[![BSD License](https://img.shields.io/pypi/l/setuptools_dynamic_dependencies.svg)](https://github.com/beeware/setuptools_dynamic_dependencies/blob/master/LICENSE)
[![Discord server](https://img.shields.io/discord/836455665257021440?label=Discord%20Chat&logo=discord&style=plastic)](https://beeware.org/bee/chat/)

`setuptools_dynamic_dependencies` is a setuptools plugin that allows you to define project
requirements that are dynamically dependent on other properties (such as project
version). This can be useful in monorepositories which contain a "core" package and a
number of "backend" packages, and you want to enforce a version dependency between the
backend and the core.

## Usage

You *must* be using a `pyproject.toml`-based project configuration. `setup.cfg` and
`setup.py` configurations are not supported.

Add `setuptools_dynamic_dependencies` to the `build-system` requirements for your project:

    [build-system]
    requires = ["setuptools_dynamic_dependencies"]

Declare "dependencies" as being dynamic in your `[project]` table:

    [project]
    dynamic = ["dependencies"]

Then, add a `[tool.setuptools_dynamic_dependencies]` section to your configuration. In
this section, add an `dependencies` key for any requirements. In the following example,
`dynamic-package` will be pinned to the same version as the package being built:

    [tool.setuptools_dynamic_requires]
    dependencies = [
        "dynamic-package == {version}"
    ]

So - if this was the `pyproject.toml` for "myproject", and you were building v1.2.3, the
dependency would be set to `dynamic_package == 1.2.3`. This `version` value can come
from a `setuptool_scm` dynamic version, if required.

You can also specify a `[tool.setuptools_dynamic_dependencies.optional-dependencies]` to
define dynamic optional requirements:

    [tool.setuptools_dynamic_dependencies.optional-dependencies]
    feature = [
        "dynamic-package == {version}"
    ]

## Community

`setuptools_dynamic_dependencies` is part of the [BeeWare suite](http://beeware.org). You
can talk to the community through:

- [@pybeeware on Twitter](https://twitter.com/pybeeware)
- [Discord](https://beeware.org/bee/chat/)

We foster a welcoming and respectful community as described in our [BeeWare
Community Code of Conduct](http://beeware.org/community/behavior/).

## Contributing

If you experience problems with `setuptools_dynamic_dependencies`, [log them on
GitHub](https://github.com/beeware/setuptools_dynamic_dependencies/issues). If you want
to contribute code, please [fork the
code](https://github.com/beeware/setuptools_dynamic_dependencies) and [submit a pull
request](https://github.com/beeware/setuptools_dynamic_dependencies/pulls).
