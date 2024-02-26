import requests
import argparse


def start():
    while True:
        text = input("Enter the text to send to the server (or type 'exit' to quit): ")
        if text.lower() == 'exit':
            break

        send_text_to_server(f'http://{args.server}:5000/send_text', text)


def send_text_to_server(server_url, text):
    data = {'text': text}
    response = requests.post(server_url, data=data)

    if response.status_code == 200:
        print("Text sent successfully")
    else:
        print("Error sending text")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Client for sending text messages to a server')
    parser.add_argument('--server', default='127.0.0.1',
                        help='Server URL to send the text message')
    args = parser.parse_args()
    start()
