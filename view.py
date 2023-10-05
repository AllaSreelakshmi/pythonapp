from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello Everyone"


if __name__ == "MY JENKINS PROJECT TASK":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
