from hardware import button_a_pressed, button_b_pressed, sleep

try:
    import microbit
    print("Using actual micro:bit buttons")
except ImportError:
    print("Using simulated buttons")
    import microbit_mock as microbit

def wait_for_input():
    """Espera hasta que un botón sea presionado y devuelve cuál fue."""
    while True:
        if button_a_pressed():
            return "A"
        elif button_b_pressed():
            return "B"
        sleep(100)