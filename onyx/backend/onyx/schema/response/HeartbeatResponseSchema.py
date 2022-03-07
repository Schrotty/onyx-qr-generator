from marshmallow import Schema, fields


class HeartbeatResponseSchema(Schema):
    host = fields.Str()
    status = fields.Str()
