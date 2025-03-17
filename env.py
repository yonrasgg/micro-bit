"""Environment detection and configuration module."""

# Determine if we're running on a real micro:bit or in development
try:
    import microbit as _test_import
    IS_MICROBIT = True
    del _test_import
except ImportError:
    IS_MICROBIT = False

if IS_MICROBIT:
    print("Running on micro:bit hardware")
else:
    print("Running in development simulation mode")
