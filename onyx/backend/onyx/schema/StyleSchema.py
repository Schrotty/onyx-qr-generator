from marshmallow import Schema, fields, validate

from onyx.schema.ColorSchema import ColorSchema
from onyx.util.styles import qr_styles


class StyleSchema(Schema):
    qr_code_style = fields.String(default='square', validate=validate.OneOf(qr_styles))
    qr_code_color = fields.Nested(nested=ColorSchema)
    qr_background_color = fields.Nested(nested=ColorSchema)
    qr_border_size = fields.Integer(default=4, validate=validate.Range(min=0, max=10))
    qr_size = fields.Integer(default=1, validate=validate.Range(min=1, max=40))
