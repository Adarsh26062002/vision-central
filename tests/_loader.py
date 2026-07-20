"""Shared importlib file-path loader for the vision-central marker modules.

The submodule has no ``__init__.py`` files next to its sources (the directories
are not Python packages). Ordinary ``import`` statements are therefore
unreliable, so every source module is loaded by *file path* via
:func:`importlib.util.spec_from_file_location`. This keeps each test isolated
and free of ``sys.path`` pollution.
"""

import importlib.util
import sys
from pathlib import Path

# Submodule root = parent of the ``tests/`` package, resolved from this file so
# the loader works regardless of the current working directory.
_ROOT = Path(__file__).resolve().parent.parent


def load_marker(name, rel_path):
    """Load and return the module at ``rel_path`` (relative to the submodule root).

    ``sys.dont_write_bytecode`` is set to ``True`` *before* execution so that no
    ``__pycache__`` directories are written next to the source files, keeping
    this pinned submodule tree pristine.
    """
    sys.dont_write_bytecode = True
    spec = importlib.util.spec_from_file_location(name, _ROOT / rel_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
