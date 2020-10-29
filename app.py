from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')
@app.route('/newsletter', methods=["GET"])
def get_data():
    data = request.get_json()
    return data

if __name__ == '__main__':
    app.run(debug=True)