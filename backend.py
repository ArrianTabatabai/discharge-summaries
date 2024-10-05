# Flask app

from flask import Flask, render_template, request, jsonify
from model import Interactor

import requests

app = Flask(__name__)

# Initialize your summarizer model
path = r"C:\Users\rajib\Documents\GitHub\discharge-summaries\saved_model" #Enter the path of the saved_model folder
i = Interactor(model_path=path)

@app.route('/')
def index():

    return render_template("index.html")


@app.route('/summarize', methods=['POST'])
def summarize():
    if request.method == 'POST':
        data = request.get_json()

        if data is None or 'inputText' not in data:
            return jsonify({'error': 'Invalid inputText'}), 400

        text = data.get('inputText')

        # Use the trainer to summarize
        summary = i.summarize(text)

        # Return summary to the frontend
        return jsonify(summary=summary)


if __name__ == '__main__':
    app.run(debug=True)
