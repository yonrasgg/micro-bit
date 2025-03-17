try:
    import microbit
    print("Using actual micro:bit display")
except ImportError:
    print("Using simulated display")
    import microbit_mock as microbit

from hardware import show_text

def show_message(message):
    """Muestra un mensaje en la pantalla LED del Micro:bit."""
    show_text(message)

def show_password(password):
    """Muestra la contraseña de manera segura (solo los primeros 5 caracteres)."""
    show_text(password[:5] + "...")
