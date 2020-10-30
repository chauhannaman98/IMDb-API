from flask import Flask, jsonify
from flask_restful import Resource, Api
from app.api.trending import Trending

app = Flask(__name__)
api = Api(app)


# A simple test api
class HelloWorld(Resource):
    def __init__(self):
        pass

    def get(self):
        return {
            'status': True,
            'response': 'Hello World!',
            'source': 'https://github.com/chauhannaman98'
        }


api.add_resource(HelloWorld, '/')
api.add_resource(Trending, '/trending')

if __name__ == '__main__':
    app.run(debug=True)
