from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "hello"

def main():
    app.run(debug=True)

if __name__ == "__main__":
    main()
