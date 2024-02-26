import argparse
from ftplib import FTP


def list_files(ftp):
    ftp.dir()


def download_file(ftp, filename):
    with open(filename, "wb") as file:
        ftp.retrbinary("RETR " + filename, file.write)


def upload_file(ftp, filename):
    with open(filename, "rb") as file:
        ftp.storbinary("STOR " + filename, file)


def main():
    parser = argparse.ArgumentParser(description="FTP client")
    parser.add_argument("--host", type=str, default="127.0.0.1", help="FTP server host")
    parser.add_argument("--port", type=int, default=21, help="FTP server port")
    parser.add_argument("--user", type=str, default="user", help="FTP username")
    parser.add_argument("--password", type=str, default="password", help="FTP password")

    args = parser.parse_args()

    ftp = FTP()
    ftp.connect(args.host, args.port)
    ftp.login(user=args.user, passwd=args.password)

    while True:
        command = input("Enter a command (list/download/upload/quit): ")

        if command == "list":
            list_files(ftp)
        elif command == "download":
            filename = input("Enter the filename to download: ")
            download_file(ftp, filename)
        elif command == "upload":
            filename = input("Enter the filename to upload: ")
            upload_file(ftp, filename)
        elif command == "quit":
            break
        else:
            print("Invalid command. Please try again.")

    ftp.quit()


if __name__ == "__main__":
    try:
        main()
    except Exception as ex:
        print("Проблемы с соединением")
        print(ex)