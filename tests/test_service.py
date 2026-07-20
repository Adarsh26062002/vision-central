"""Unit tests for the vision-central marker: service.py::run().

Scope note: this submodule owns exactly one in-scope marker (``run()``). Paths
excluded by this submodule's ``.blitzyignore`` (``build/**``) and by the
superproject's ignore policy are not imported or tested here. The nested
``nested-utils`` submodule has its own self-contained suite.
"""

import inspect
import unittest

from tests._loader import load_marker

run = load_marker("service", "service.py").run
EXPECTED = "vision-central: always included"


class TestService(unittest.TestCase):
    """Contract tests for the ``run()`` marker function."""

    def test_run_returns_marker(self):
        # Byte-exact oracle: the marker string is its own source of truth.
        self.assertEqual(run(), EXPECTED)

    def test_run_returns_str(self):
        self.assertIsInstance(run(), str)

    def test_run_non_empty(self):
        self.assertNotEqual(run(), "")

    def test_run_is_deterministic(self):
        # Idempotency: repeated calls return equal values (no hidden state).
        self.assertEqual(run(), run())

    def test_run_zero_arg_signature(self):
        # Lock in the parameterless design.
        self.assertEqual(len(inspect.signature(run).parameters), 0)


if __name__ == "__main__":
    unittest.main()
