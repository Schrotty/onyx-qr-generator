from marshmallow import Schema, fields, validate


class ColorSchema(Schema):
    red = fields.Integer(default=255, required=True, validate=validate.Range(min=0, max=255))
    green = fields.Integer(default=255, required=True, validate=validate.Range(min=0, max=255))
    blue = fields.Integer(default=255, required=True, validate=validate.Range(min=0, max=255))
