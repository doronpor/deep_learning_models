"""Basic tests to verify the test suite is working."""


def test_pytest_works():
    """Verify that pytest is working correctly."""
    assert True, "Basic test should pass"


def test_python_environment():
    """Verify that Python environment is set up correctly."""
    import sys

    assert sys.version_info.major == 3, "Python 3 is required"
    assert sys.version_info.minor >= 9, "Python 3.9 or higher is required"
