try:
    from flask_restful import Resource
    from flask import jsonify, request
    from datetime import date
    from app.services.search import (
        searchByTitle,
        searchByName,
    )
except e:
    print('Caught exception while importing: {}'.format(e))


class Search(Resource):
    def get(self):

        args = request.args
        q = args['q']
        q_type = args['stype']

        if(q_type == 'title'):
            response = searchByTitle.searchByTitle(q)
        elif(q_type == 'name'):
            response = searchByName.searchByName(q)

        return jsonify({
            'status': True,
            'date': str(date.today().strftime("%b-%d-%Y")),
            'search-results': response
        })
