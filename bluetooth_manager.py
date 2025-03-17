try:
    # Try to import from actual microbit
    import microbit
    from microbit import uart
    print("Running on micro:bit hardware")
except ImportError:
    # Import from mock for development
    print("Running in development mode with mock microbit")
    from microbit_mock import uart
    import microbit_mock as microbit

from hardware import init_bluetooth, send_bluetooth, show_text

def send_password(password):
    """Envía la contraseña generada a un dispositivo vía Bluetooth."""
    try:
        # Initialize UART over BLE
        init_bluetooth(baudrate=9600)
        # Send password
        send_bluetooth(password)
        show_text("Sent!")
    except Exception as e:
        show_text("Error")
        print("Error al enviar: ", e)
