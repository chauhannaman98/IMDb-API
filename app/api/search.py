from flask_restful import Resource
from flask import jsonify, request
from datetime import date
from app.services.search import (
    searchByTitle,
    searchByName,
)


class SearchByTitle(Resource):
    def get(self):

        args = request.args
        title = args['q']

        return jsonify({
            'status': True,
            'date': str(date.today().strftime("%b-%d-%Y")),
            'search-results': searchByTitle.searchByTitle(title)
        })


class SearchByName(Resource):
    def get(self):

        args = request.args
        name = args['q']

        return jsonify({
            'status': True,
            'date': str(date.today().strftime("%b-%d-%Y")),
            'search-results': searchByName.searchByName(name)
        })
