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

        args = request.args
        q_type = args['type']

        if(q_type == 'title'):
            response_obj = getById.GetTitleById()
            response = response_obj.getById()
            success = True
        elif(q_type == 'name'):
            response_obj = getById.GetNameById()
            response = response_obj.getById()
            success = True
        else:
            response = 'query type not supported'
            success = False

        return jsonify({
            'success': success,
            'response': response
        })
