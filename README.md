pandas-dev-flaker
=================

Plugin for `flake8` used to contribute to [pandas](https://github.com/pandas-dev/pandas).

NOTE: this is not a linter meant for pandas usage, but for pandas development. If you want
a linter for pandas usage, please see [pandas-vet](https://github.com/deppen8/pandas-vet).

## installation

`pip install pandas-dev-flaker`

## flake8 codes

| Code   | Description                 |
|--------|-----------------------------|
| PDF001 | import from collections.abc (use 'from collections import abc' instead) |
| PDF002 | pd.api.types used (import from pandas.api.types instead)                |
| PDF003 | pytest.raises used without 'match='                                     |
| PDF004 | builtin filter function used                                            |
| PDF005 | 'pytest.raises' used outside of context manager                         |
| PDF006 | builtin exec used                                                       |
| PDF007 | 'pytest.warns' used (use 'tm.assert_produces_warning' instead)          |
| PDF008 | 'foo.__class__' used, (use 'type(foo)' instead)                         |
| PDF009 | 'common' imported from 'pandas.core' without 'comm' alias               |
| PDF010 | import from 'conftest' found                                            |

## contributing

### development environment

Make sure you have installed [tox](https://tox.readthedocs.io/en/latest/install.html). Then, do

```bash
tox --devenv venv
. venv/bin/activate
pip install pre-commit
pre-commit install
```

and you will be in a virtual environment with all the dependencies you'll need installed.

### new rules

Each new linting rule should be its own file inside `pandas-dev-flaker/_plugins`. Please linting rule should have two sets of tests in `pandas-dev-flaker/tests` - one for when the linting rule is expected to pass, and another for when it's expected to fail.

## credit

Several methods are simplified versions of methods from [pyupgrade](https://github/asottile/pyupgrade) - please find their license in the `LICENSES` folder.

## as a pre-commit hook

See [pre-commit](https://github.com/pre-commit/pre-commit) for instructions

Sample `.pre-commit-config.yaml`:

```yaml
-   repo: https://github.com/pycqa/flake8
    rev: 3.9.0
    hooks:
    -   id: flake8
        additional_dependencies: [pandas-dev-flaker==0.0.1]
```
