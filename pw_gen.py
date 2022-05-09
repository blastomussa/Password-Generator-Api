from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

#needs UTF or ASCII switch and defaults
#needs special character switch
#needs good random module
#needs good english dictionary
#needs string len min and max
#human readable or gibberish
#number of upper and lower
#number of special chacters
#number of integers
#choose where uppercase letters are; beginning, end, random
#needs defaults for everything; call with no variables should work
#no puts/deletes/posts only get
#api throttling so I dont get DOSed
#bulk; output csv for download
#how do I run app on namecheap host under blastomussa.dev domain?

class hello(Resource):
    def get(self):
        return {"data": "Hello World"}

api.add_resource(hello, "/hello")

if __name__ == '__main__':
    app.run(debug=True)
