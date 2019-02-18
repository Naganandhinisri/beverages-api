from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def home():
    return "Hello world"


@app.route('/post-data', methods=['POST'])
def get_data():
    print(request)
    return "Hello world"


if __name__ == '__main__':
    app.run()
