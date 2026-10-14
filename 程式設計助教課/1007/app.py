from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Docker Flask!"

@app.route("/evan")
def evan():
    return "Evan happy birthday!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)