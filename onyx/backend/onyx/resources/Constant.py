import logging

from flask_apispec import MethodResource, doc, marshal_with, use_kwargs
from flask_restful import Resource

from onyx.QRBuilder import build_response
from onyx.schema.request.GeneratorRequestSchema import GeneratorRequestSchema
from onyx.schema.response.GeneratorResponseSchema import GeneratorResponseSchema
from onyx.util.StructMessage import StructMessage


class Constant(MethodResource, Resource):

    @doc(description='Endpoint for generating a static qr code.', tags=['Static QR'])
    @use_kwargs(GeneratorRequestSchema, location='json')
    @marshal_with(schema=GeneratorResponseSchema, code=201, description='Response containing the generated qr code as base64 '
                                                                        'encoded image string and the encode data in plain text.')
    def post(self, payload, style=None, **kwargs):
        logging.info(StructMessage(message='Received qr request', payload=payload, style=style, persistent=False))
        return build_response(payload, style=style, persistent=False)
