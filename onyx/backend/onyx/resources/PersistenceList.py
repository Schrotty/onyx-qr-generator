import logging

from flask_apispec import MethodResource, doc, use_kwargs, marshal_with
from flask_restful import Resource

from onyx.QRBuilder import build_response
from onyx.util.StructMessage import StructMessage
from onyx.schema.response.GeneratorResponseSchema import GeneratorResponseSchema
from onyx.schema.request.PersistenceRequestSchema import PersistenceRequestSchema


class PersistenceList(MethodResource, Resource):

    @doc(description='Endpoint for generating a qr code with persistent payload.', tags=['Persistent QR'])
    @use_kwargs(PersistenceRequestSchema, location='json')
    @marshal_with(schema=GeneratorResponseSchema, code=201, description='Response containing the generated qr code as base64 encoded image string and the encode url to fetch the persistent payload.')
    def post(self, payload, style=None, **kwargs):
        logging.info(StructMessage(message='Received persistent qr request', payload=payload, style=style, persistent=True))
        return build_response(payload, style=style, persistent=True)
