try:
    import tomllib
except ImportError:
    import tomli as tomllib


def finalize_dependencies(dist):
    """Parse any dynamic dependencies from the pyproject.toml file."""
    # Load the config file.
    with open("pyproject.toml") as f:
        pyproject = tomllib.loads(f.read())

    # Dynamic configuration is in [tool.setuptools_dynamic_dependencies]
    dynamic_requires = pyproject.get("tool", {}).get(
        "setuptools_dynamic_dependencies", {}
    )

    # [tool.setuptools_dynamic_dependencies]
    # dependencies = [
    #     "dynamic-package == {version}"
    # ]
    substitutions = {"version": dist.metadata.version}
    dist.install_requires = [
        requirement.format(**substitutions)
        for requirement in dynamic_requires.get("dependencies", [])
    ]

    # [tool.setuptools_dynamic_dependencies.optional-dependencies]
    # feature = [
    #     "dynamic-package == {version}"
    # ]
    dist.extras_require = {
        extra: [requirement.format(**substitutions) for requirement in requirements]
        for extra, requirements in dynamic_requires.get(
            "optional-dependencies", {}
        ).items()
    }


# Make the requirements get executed last, to make sure that version has been computed.
finalize_dependencies.order = 1000
