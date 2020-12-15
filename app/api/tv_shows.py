try:
    from flask_restful import Resource
    from flask import jsonify, request
    from app.scrappers.tv_shows import (
        tvShowsTop250,
    )
except Exception as e:
    print('Caught exception while importing: {e}')


class TVShows(Resource):
    def get(self):

        print('tv-shows')

        args = request.args
        find = args['find']

        if find == 'top-rated':
            response = tvShowsTop250.getTop250Shows()
            status = True
        else:
            status = False
            response = 'Unable to fetch data'

        return jsonify({
            'success': status,
            'top250': response
        })
