from flask_restful import Resource
from flask import jsonify
from datetime import date
from app.services.tv_shows import (
    tvShowsTop250,
)


class Top250(Resource):
    def get(self):
        return jsonify({
            'status': True,
            'date': str(date.today().strftime("%b-%d-%Y")),
            'top250': tvShowsTop250.getTop250Shows()
        })
