from flask_restful import Resource
from app.services.tvShowsTop250 import main


class Top250(Resource):
    def get(self):
        return {
            'api': 'top-250',
            'status': True,
            'top250': main()
        }
