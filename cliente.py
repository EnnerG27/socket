import socket
import sys

# Crear un socket TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectarse al servidor
host = "localhost"  # Cambiar a la dirección IP del servidor si es necesario
port = 8000

try:
    sock.connect((host, port))
except socket.error as msg:
    print(f"Error al conectar con el servidor: {msg}")
    sys.exit()

# Enviar un mensaje al servidor
sock.sendall(b"Hola desde el cliente!")

# Recibir la respuesta del servidor
data = sock.recv(1024)
if not data:
    print("El servidor se ha cerrado")
else:
    print(f"Recibido del servidor: {data.decode('utf-8')}")

# Cerrar el socket
sock.close()
