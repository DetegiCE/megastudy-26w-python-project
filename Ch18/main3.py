from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return "hello"

@app.route('/map')
def map():
    return render_template('univ_map.html')

def main():
    app.run(debug=True)

if __name__ == "__main__":
    main()
