import logging
import os

from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask import Flask
from flask_apispec import FlaskApiSpec
from flask_restful import Api
from flask_swagger_ui import get_swaggerui_blueprint
from webargs.flaskparser import parser, abort

from onyx.resources.Heartbeat import Heartbeat
from onyx.util.utils import decode_log_level
from onyx.util.StructMessage import StructMessage
from onyx.resources.Persistence import Persistence
from onyx.resources.PersistenceList import PersistenceList
from onyx.resources.Constant import Constant

app = Flask(__name__)
app.register_blueprint(get_swaggerui_blueprint('/api/spec/ui', '/api/spec/'))
app.config.update({
    'APISPEC_SPEC': APISpec(title='Onyx - QR-Generator', version='v1', plugins=[MarshmallowPlugin()],
                            openapi_version='2.0.0'),

    'APISPEC_SWAGGER_URL': '/api/spec/'
})

api = Api(app)
docs = FlaskApiSpec(app)

# configure logging
logging.basicConfig(level=decode_log_level(os.getenv('ONYX_LOG_LEVEL', 'DEBUG')), format='%(message)s')

# register api resources
api.add_resource(Heartbeat, '/', '/api/heartbeat')
api.add_resource(Constant, '/api/static')
api.add_resource(PersistenceList, '/api/persistence')
api.add_resource(Persistence, '/api/persistence/<identifier>')

# register api docs
docs.register(Heartbeat)
docs.register(Constant)
docs.register(Persistence)
docs.register(PersistenceList)

# log app startup
logging.info(StructMessage(message='Onyx started', persistent=bool(os.getenv('ONYX_ENABLE_REDIS'))))


# register error handler for marshmallow errors
@parser.error_handler
def handle_request_parsing_error(err, req, schema, *, error_status_code, error_headers):
    logging.warning(StructMessage(message='Received unprocessable request', error=err.messages))
    abort(422, errors=err.messages)


if __name__ == '__main__':
    app.run(debug=True, port=8080)
