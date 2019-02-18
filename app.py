import psycopg2
from flask import Flask, request, render_template
from flask_cors import CORS

from modules.post_data_to_database import post_data

app = Flask(__name__)
CORS(app)
connection = psycopg2.connect("dbname=cafeteria user=postgres")


@app.route('/')
def home():
    return render_template('homepage.html')


@app.route('/post-data', methods=['POST'])
def get_data():
    post_data(connection, request.form)
    return render_template('detailspage.html', shared=request.form)


if __name__ == '__main__':
    app.run()
