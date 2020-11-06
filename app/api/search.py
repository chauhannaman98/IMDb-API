try:
    from flask_restful import Resource
    from flask import jsonify, request
    from datetime import date
    from app.services.search import (
        searchByTitle,
        searchByName,
    )
except Exception as e:
    print('Caught exception while importing: {}'.format(e))


class Search(Resource):
    def get(self):

        args = request.args
        q = args['q']
        q_type = args['stype']

        if(q_type == 'title'):
            response_obj = searchByTitle.SearchByTitle()
            response = response_obj.searchByTitle(q)
            docs = 'title'
        elif(q_type == 'name'):
            response_obj = searchByName.SearchByName()
            response = response_obj.searchByName(q)
            docs = 'name'

        return jsonify({
            'status': True,
            'date': str(date.today().strftime("%b-%d-%Y")),
            'docs': 'https://github.com/chauhannaman98/IMDb-API#search-by-{}'.format(docs),
            'search-results': response
        })
