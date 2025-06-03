"""Test version information."""


def test_version():
    """Verify that version information is available."""
    from deep_learning_models import __version__

    assert isinstance(__version__, str), "Version should be a string"
    assert len(__version__.split(".")) == 3, "Version should be in format X.Y.Z"
