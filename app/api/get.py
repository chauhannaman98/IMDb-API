try:
    from flask_restful import Resource
    from flask import jsonify, request
    from app.scrappers.get import (
        getById
    )
except Exception as e:
    print('Caught exception while importing: {}'.format(e))

class Get(Resource):
    def get(self):
        response_obj = getById.GetById()
        response = response_obj.getById()
        print(response)
        print(type(response))
        return jsonify({
            'success': True,
            'response': response
        })
