from flask_restful import Resource, reqparse

from onyx.Generator import generate_code

parser = reqparse.RequestParser()
parser.add_argument('payload', required=True, type=str, help='The payload for the qr code')


class BasicCode(Resource):
    def post(self):
        args = parser.parse_args()
        return {'image': generate_code(args['payload'])}
