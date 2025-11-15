# from ._version import version as __version__

# __all__ = []

try:
    from ._version import version as __version__
except ImportError:
    # Fallback for editable installs before version file exists
    __version__ = "0.0.0"
