import logging
import socket

from flask import jsonify
from flask_apispec import marshal_with, MethodResource, doc
from flask_restful import Resource

from onyx.schema.response.HeartbeatResponseSchema import HeartbeatResponseSchema
from onyx.util.StructMessage import StructMessage


class Heartbeat(MethodResource, Resource):

    @doc(description='Request an api heartbeat.', tags=['Heartbeat'])
    @marshal_with(schema=HeartbeatResponseSchema, code=200, description='Response containing host and current status.')
    def get(self):
        logging.info(StructMessage(message='Received heartbeat request'))
        return jsonify(dict(host=socket.getfqdn(), status="online"))
