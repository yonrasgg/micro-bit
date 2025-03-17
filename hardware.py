"""Hardware abstraction layer for micro:bit functionality."""
from env import IS_MICROBIT
import time

# Only import microbit related modules when running on actual hardware
if IS_MICROBIT:
    import microbit
    from microbit import button_a, button_b, display, uart, sleep as _sleep
else:
    # Mock implementations for development
    class MockDisplay:
        def scroll(self, text):
            print(f"[DISPLAY] Scrolling: {text}")
        
        def set_pixel(self, x, y, brightness):
            print(f"[DISPLAY] Set pixel at ({x},{y}) to brightness {brightness}")

    class MockButton:
        def __init__(self, name):
            self.name = name
        
        def was_pressed(self):
            return input(f"Press 'y' if button {self.name} was pressed: ").lower() == 'y'

    class MockUart:
        def init(self, baudrate=9600, tx=None, rx=None):
            print(f"[UART] Initialized with baudrate {baudrate}")
        
        def write(self, data):
            if isinstance(data, bytes):
                print(f"[UART] Sending: {data.decode('utf-8', errors='replace')}")
            else:
                print(f"[UART] Sending: {data}")
    
    display = MockDisplay()
    button_a = MockButton('A')
    button_b = MockButton('B')
    uart = MockUart()
    
    def _sleep(ms):
        time.sleep(ms / 1000)

# Unified functions that work in both environments
def sleep(ms):
    _sleep(ms)

def show_text(text):
    display.scroll(text)

def set_pixel(x, y, brightness):
    display.set_pixel(x, y, brightness)

def button_a_pressed():
    return button_a.was_pressed()

def button_b_pressed():
    return button_b.was_pressed()

def init_bluetooth(baudrate=9600):
    uart.init(baudrate=baudrate, tx=None, rx=None)

def send_bluetooth(data):
    if not IS_MICROBIT and isinstance(data, str):
        data = data.encode()
    uart.write(data)
