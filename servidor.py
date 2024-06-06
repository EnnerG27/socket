import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "localhost"
port = 8000

try:
    sock.bind((host, port))
except socket.error as msg:
    print(f"Error al enlazar el socket: {msg}")
    sys.exit()

sock.listen(1)

print("Esperando conexiones...")
client_sock, address = sock.accept()
print(f"Conectado con: {address}")

while True:
    try:
        data = client_sock.recv(1024)
        if not data:
            break
        print(f"Recibido del cliente: {data.decode('utf-8')}")

        client_sock.sendall(b"Hola profesor erving desde el servidor!")
    except socket.error as msg:
        print(f"Error al enviar o recibir datos: {msg}")
        break

client_sock.close()
sock.close()
