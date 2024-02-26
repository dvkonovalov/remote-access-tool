import socket
import argparse


def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((args.host, args.port))

    while True:
        data = client_socket.recv(1024)
        print(data.decode())

        message = input('Enter message: ')
        if message == 'exit':
            break

        client_socket.send(message.encode())

    client_socket.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Telnet client')
    parser.add_argument('--host', default='127.0.0.1', help='Host IP address')
    parser.add_argument('--port', type=int, default=23, help='Port number')
    args = parser.parse_args()
    main()