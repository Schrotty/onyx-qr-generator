import logging
import socket

from flask import jsonify
from flask_apispec import marshal_with, MethodResource, doc
from flask_restful import Resource

from onyx.schema.response.HeartbeatResponseSchema import HeartbeatResponseSchema
from onyx.util.StructMessage import StructMessage


class Heartbeat(MethodResource, Resource):

    @doc(description='Request an heartbeat. Used for checking status and kubernetes/ GCEs probes.', tags=['Heartbeat'])
    @marshal_with(schema=HeartbeatResponseSchema, code=200, description='Response containing hostname and current status of the pod answering the request.')
    def get(self):
        logging.info(StructMessage(message='Received heartbeat request.'))
        return jsonify(dict(host=socket.getfqdn(), status="online"))
