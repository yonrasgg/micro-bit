# Micro:bit Password Generator and Manager

## Project Structure
/Proyecto_MicroBit
│── main.py                # Archivo principal que ejecuta el menú y la lógica general
│── password_generator.py  # Módulo para la generación de contraseñas seguras
│── bluetooth_manager.py   # Módulo para la comunicación Bluetooth
│── display_manager.py     # Módulo para manejar la pantalla LED
│── button_manager.py      # Módulo para la gestión de los botones
│── utils.py               # Funciones auxiliares comunes
│── config.py              # Configuración de parámetros del sistema
│── microbit_mock.py       # Simulador del módulo microbit para desarrollo

## Functionality
- Button A: Generate a new secure password
- Button B: Send the last generated password via Bluetooth

## Error Handling
- Prevents sending when no password has been generated
- Provides feedback on success/failure of operations

## Development & Deployment

### Development Mode
This code can be run on your computer for testing using the mock microbit module:
```bash
python main.py
```

### Deployment to micro:bit
To deploy the code to your micro:bit device:

1. Install the required tools:
   ```bash
   pip install uflash microfs
   ```

2. Connect your micro:bit via USB

3. Flash the code:
   ```bash
   uflash main.py
   ```

4. Transfer additional files:
   ```bash
   microfs put password_generator.py
   microfs put bluetooth_manager.py
   microfs put display_manager.py
   microfs put button_manager.py
   microfs put utils.py
   microfs put config.py
   ```