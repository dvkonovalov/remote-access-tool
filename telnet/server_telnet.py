import socket


def main():
    HOST = '127.0.0.1'  # Локальный хост
    PORT = 23  # Порт для telnet

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)

    print(f'Server started on {HOST}:{PORT}')

    while True:
        client_socket, addr = server_socket.accept()
        print(f'Connected to {addr}')

        client_socket.send(b"Welcome to the telnet server!\n")

        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            print(f'Received: {data.decode()}')
            response = f'You sent: {data.decode()}'
            client_socket.send(response.encode())

        print(f'Disconnected from {addr}')
        client_socket.close()


if __name__ == '__main__':
    main()