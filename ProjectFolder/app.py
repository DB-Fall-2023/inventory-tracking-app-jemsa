from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import psycopg2
from Handlers.parts_handler import parts_handler

conn = psycopg2.connect(
    database="dao09k51u783e5",
    user="aubzwnpircvyvo",
    password="ac0be2f0a0beccd6359cfc837765b3d6d8fb3b6c7bbffcda2aaaacac84e752bc",
    host="ec2-44-214-132-149.compute-1.amazonaws.com",
    port="5432"
)
#Test DB
#database="dbproject",
#user="postgres",
#password="postgres"
#host="localhost"
#port="38119"


app = Flask(__name__)
# Apply CORS to this app
CORS(app)


app.register_blueprint(parts_handler, url_prefix='/jemsa/parts')

if __name__ == '__main__':
    app.run(debug=True)