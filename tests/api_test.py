from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

get_args = reqparse.RequestParser()
get_args.add_argument("type", type=str, help="UTF or ASCII")


        #args = get_args.parse_args()
#https://stackoverflow.com/questions/30779584/flask-restful-passing-parameters-to-get-request
#use marshmello?
@api.resource('/')
class Foo(Resource):
    def get(self):
        args = get_args.parse_args()
        return args

if __name__ == '__main__':
    app.run(debug=True)
