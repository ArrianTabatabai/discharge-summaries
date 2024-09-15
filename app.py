# Flask app

from flask import Flask, render_template, request, jsonify
from summarizer import alpha
from trainer import ModelTrainer

app = Flask(__name__)

# Initialize your summarizer model
summarizer_model = alpha()
trainer_model = ModelTrainer()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    if request.method == 'POST':
        # Get input text from the user (e.g., patient documents)
        text = request.form['inputText']
        
        # Use the trainer to summarize
        summary = trainer_model.summarize(text)
        
        # Return summary to the frontend
        return jsonify(summary=summary[0]["generated_text"][1]["content"])

if __name__ == '__main__':
    app.run(debug=True)