from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

def main():
    authorizer = DummyAuthorizer()
    authorizer.add_user("user", "password", ".", perm="elradfmwMT")

    handler = FTPHandler
    handler.authorizer = authorizer

    address = ("127.0.0.1", 21)

    server = FTPServer(address, handler)
    server.serve_forever()

if __name__ == "__main__":
    main()