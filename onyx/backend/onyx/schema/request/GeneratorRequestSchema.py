from marshmallow import Schema, fields

from onyx.schema.StyleSchema import StyleSchema


class GeneratorRequestSchema(Schema):
    payload = fields.String(default='Hello there', required=True, desciption='The payload of the qr code in plain text.')
    style = fields.Nested(nested=StyleSchema, required=False, description='Optional style parameter for the qr code.')
