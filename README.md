# vision-central

A dependency-free Git-submodule fixture used by the **blitzyignore-submodule-test**
superproject to verify that `.blitzyignore` scoping never leaks across submodule
boundaries. This submodule declares its own `.blitzyignore` that ignores
`build/**`, and it contains a further nested submodule, **nested-utils**.

## Marker function

The marker is a pure, zero-argument function that returns a constant string.
The string is its own verification oracle.

| Function | Module | Returns |
|----------|--------|---------|
| `run()` | `service.py` | `vision-central: always included` |

## Nested submodule

`nested-utils` is a separate submodule with its own self-contained test suite
(`nested-utils/tests/`). Its `build/generated.py` marker is deliberately
**INCLUDED**: this submodule's `build/**` ignore rule is scoped to *this*
subtree and must not leak into the nested submodule. See `nested-utils/README.md`.

## Tests

Standard-library `unittest` tests live in `tests/`. They add **no runtime and no
test-framework dependency** — the submodule stays zero-dependency. The source
module is loaded by file path via `importlib` (see `tests/_loader.py`) so the
non-package layout is handled reliably and no `sys.path` pollution occurs.

| Test file | Covers |
|-----------|--------|
| `tests/test_service.py` | `service.py::run()` — exact value, type, non-empty, determinism, zero-arg signature |

### Run the tests

From the submodule root:

```sh
PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests -v
```

Run the nested-utils suite separately, from its own root:

```sh
cd nested-utils && PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests -v
```

Single test:

```sh
python -m unittest tests.test_service.TestService.test_run_returns_marker
```

Optional coverage (developer-only; keep the data file outside the tree):

```sh
COVERAGE_FILE=/tmp/vc_cov/.coverage coverage run -m unittest discover -s tests
coverage report -m
```

## Excluded from tests

The `build/**` subtree (per this submodule's `.blitzyignore`) and any paths
excluded by the superproject's ignore policy are intentionally left out and are
**never** imported, tested, or measured.
