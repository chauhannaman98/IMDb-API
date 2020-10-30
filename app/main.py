from flask import Flask, jsonify
from flask_restful import Resource, Api
from app.api.tv_shows import Top250

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
api.add_resource(Top250, '/tv-shows/top250')

if __name__ == '__main__':
    app.run(debug=True)
