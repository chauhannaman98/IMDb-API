try:
    from flask_restful import Resource
    from flask import jsonify, request
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
            docs = '/#search-by-title'
            success = True
        elif(q_type == 'name'):
            response_obj = searchByName.SearchByName()
            response = response_obj.searchByName(q)
            docs = '/#search-by-name'
            success = True
        else:
            obj = "400: Bad request"
            docs = '/'
            success = False

        return jsonify({
            'success': success,
            'docs': 'https://chauhannaman98.github.io/IMDb-API{}'.format(docs),
            'search-results': response
        })
