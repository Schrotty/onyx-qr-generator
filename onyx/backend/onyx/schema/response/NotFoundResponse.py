from marshmallow import Schema, fields


class NotFoundResponse(Schema):
    message = fields.String(description='Error message when identifier is not existing.')
