from flask_restful import Resource
# from app.services.getTrendings import main


class Trending(Resource):
    def get(self):
        return {
            'api': 'trending',
            'status': True,
            # 'trending': show()
        }
