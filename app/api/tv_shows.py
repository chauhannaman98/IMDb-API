from flask_restful import Resource
from flask import jsonify
from app.services.tv_shows import (
    tvShowsTop250,
)


class Top250(Resource):
    def get(self):
        return jsonify({
            'success': True,
            'top250': tvShowsTop250.getTop250Shows()
        })
