from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to the speech-to-text flask app!"


if __name__ == "__main__":
    app.run(debug=True)
