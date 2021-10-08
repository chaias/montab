import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from resources.montab import Montab,MontabList

app = Flask(__name__)

app.config['DEBUG'] = True
#orcl.mosi.com.gt
app.config['SQLALCHEMY_DATABASE_URI'] = 'oracle://SCI:SCI@192.9.200.12:1521/orcl'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'mosicmf'
api = Api(app)

#jwt = JWT(app, authenticate, identity)  # /auth

api.add_resource(Montab, '/montab/<moncod>')
api.add_resource(MontabList, '/montab')

if __name__ == '__main__':
    from db import db
    db.init_app(app)

    #if app.config['DEBUG']:
    #    @app.before_first_request
    #    def create_tables():
    #        db.create_all()

    app.run(port=5000)
