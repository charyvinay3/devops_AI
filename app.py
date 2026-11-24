from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Calculator Application Running"

@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    return str(a + b)

@app.route("/health")
def health():
    return "UP"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)