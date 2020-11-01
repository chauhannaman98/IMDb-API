from flask_restful import Resource
from flask import jsonify, request
from datetime import date
from app.services.searchByTitle import searchByTitle


class SearchByTitle(Resource):
    def get(self):

        args = request.args
        title = args['q']

        return jsonify({
            'status': True,
            'date': str(date.today().strftime("%b-%d-%Y")),
            'search-results': searchByTitle(title)
        })
