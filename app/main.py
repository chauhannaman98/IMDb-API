from flask import Flask, jsonify, request
from datetime import date
from flask_restful import Resource, Api
from app.api.tv_shows import Top250

app = Flask(__name__)
api = Api(app)


class Home(Resource):
    def __init__(self):
        pass

    def get(self):
        return jsonify({
            'status': True,
            'date': str(date.today().strftime("%b-%d-%Y")),
            'source': 'https://github.com/chauhannaman98/IMDb-API',
            'api-services-available': {
                'Top25 TV Shows': request.base_url+'tv-shows/top250',
            }
        })


api.add_resource(Home, '/')
api.add_resource(Top250, '/tv-shows/top250')

if __name__ == '__main__':
    app.run(debug=True)
