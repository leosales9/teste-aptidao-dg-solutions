from os import environ
from flask import Flask
from flask import request
from flask_cors import CORS
from database.postgres_connection import PostgresConnection
from controllers.people import PeopleController


postgres = PostgresConnection(
    host=environ.get('POSTGRES_HOST', 'localhost'),
    user=environ.get('POSTGRES_USER', 'root'),
    password=environ.get('POSTGRES_PASSWORD', 'root'),
    database=environ.get('POSTGRES_DB', 'people')).get_connection()
controller = PeopleController(postgres)

app = Flask(__name__)
CORS(app)


@app.route('/people/list', methods=['GET'])
def list_people():
    return controller.get_people()


@app.route('/people/create', methods=['POST'])
def create_people():
    return controller.create_person(request.get_json())


@app.route('/people/remove/<people_id>', methods=['DELETE'])
def remove_people(people_id):
    return controller.remove_person(people_id)
