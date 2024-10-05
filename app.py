from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

# test.py functionality integrated
@app.route('/summary')
def get_summary():
    # Replace this with your current URL and file path
    raw_url = 'https://acbf-86-10-113-94.ngrok-free.app/'
    req_url = raw_url + "/summarize"
    path = r"C:\Users\bahar\Synopsis AI\discharge-summaries\Example Training\2 (Single File Format)\input"

    text = open(path, "r").read()

    data = {
        'inputText': text
    }
    response = requests.post(req_url, json=data)

    # Extract the JSON output
    return jsonify(response.json())

# Route to render the web page
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)