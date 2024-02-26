from flask import Flask, request

app = Flask(__name__)

@app.route('/send_text', methods=['POST'])
def send_text():
    text = request.form['text']
    print(f"Received text: {text}")
    return "Text received successfully"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)