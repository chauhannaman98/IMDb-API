from flask_restful import Resource
from datetime import date
from app.services.tvShowsTop250 import getTop250Shows


class Top250(Resource):
    def get(self):
        return {
            'status': True,
            'date': str(date.today().strftime("%b-%d-%Y")),
            'top250': getTop250Shows()
        }
