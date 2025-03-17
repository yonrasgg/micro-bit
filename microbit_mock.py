"""Mock implementation of microbit module for development purposes."""

class Display:
    def scroll(self, text):
        print(f"[DISPLAY] Scrolling: {text}")
    
    def set_pixel(self, x, y, brightness):
        print(f"[DISPLAY] Set pixel at ({x},{y}) to brightness {brightness}")

class Button:
    def __init__(self, name):
        self.name = name
        self._pressed = False
    
    def was_pressed(self):
        # In development mode, simulate button press via input
        response = input(f"Was button {self.name} pressed? (y/n): ")
        return response.lower() == 'y'

class Uart:
    def init(self, baudrate=9600, tx=None, rx=None):
        print(f"[UART] Initialized with baudrate {baudrate}")
    
    def write(self, data):
        if isinstance(data, bytes):
            print(f"[UART] Sending: {data.decode('utf-8', errors='replace')}")
        else:
            print(f"[UART] Sending: {data}")

# Create instances
display = Display()
button_a = Button('A')
button_b = Button('B')
uart = Uart()

def sleep(ms):
    import time
    time.sleep(ms / 1000)
    
def panic(error_code):
    print(f"[PANIC] Error code: {error_code}")
