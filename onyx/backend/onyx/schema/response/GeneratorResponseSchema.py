from marshmallow import Schema, fields


class GeneratorResponseSchema(Schema):
    status = fields.String(description='Result of the operation.')
    image = fields.String(description='The base64 encoded qr code image.')
    payload = fields.String(description='The content encoded in the qr code or when failed the error message.')
