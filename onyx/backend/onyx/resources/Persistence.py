from flask import render_template, Response
from flask_apispec import MethodResource, doc, marshal_with, use_kwargs
from flask_restful import Resource, abort

from onyx.util.StorageEntity import StorageEntity
from onyx.util.utils import decode_mime_type
from onyx.schema.response.DeleteResponse import DeleteResponse
from onyx.schema.response.NotFoundResponse import NotFoundResponse
from onyx.schema.request.PersistenceUpdateRequestSchema import PersistenceUpdateRequestSchema
from onyx.schema.response.PersistenceUpdateResponseSchema import PersistenceUpdateResponseSchema


class Persistence(MethodResource, Resource):

    @doc(description='Get persistent qr content.', tags=['Persistent QR'])
    def get(self, identifier, **kwargs):
        self.identifier_exists(identifier)
        storage_data = StorageEntity.load(identifier)
        template = f"{decode_mime_type(storage_data['mime_type'])}.html"
        return Response(render_template(template, content=storage_data['data']), mimetype='text/html')

    @doc(desciprion='Delete persistent qr content.', tags=['Persistent QR'])
    @marshal_with(DeleteResponse, code=204)
    @marshal_with(NotFoundResponse, code=404)
    def delete(self, identifier, **kwargs):
        self.identifier_exists(identifier)
        StorageEntity.delete(identifier)
        return None, 204

    @doc(desciprion='Update persistent qr content.', tags=['Persistent QR'])
    @marshal_with(PersistenceUpdateResponseSchema, code=200)
    @use_kwargs(PersistenceUpdateRequestSchema, location='json')
    def put(self, identifier, value, mime_type, **kwargs):
        self.identifier_exists(identifier)
        if StorageEntity.save(identifier, {'data': value, 'mime_type': mime_type}):
            return {
                'identifier': identifier,
                'value': StorageEntity.load(identifier)
            }

        return None, 204

    @staticmethod
    def identifier_exists(identifier):
        if not StorageEntity.exists(identifier):
            abort(404)
