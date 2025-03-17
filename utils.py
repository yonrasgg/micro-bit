try:
    import microbit
    print("Using actual micro:bit hardware")
except ImportError:
    print("Using simulated micro:bit")
    import microbit_mock as microbit

from hardware import set_pixel, sleep

def blink_led():
    """Hace parpadear un LED en la posición central."""
    for _ in range(3):
        set_pixel(2, 2, 9)
        sleep(500)
        set_pixel(2, 2, 0)
        sleep(500)

def save_last_password(password):
    """Guarda la última contraseña generada en la memoria."""
    try:
        with open("last_password.txt", "w") as file:
            file.write(password)
        return True
    except:
        return False
