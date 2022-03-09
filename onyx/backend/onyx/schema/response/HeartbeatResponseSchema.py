from marshmallow import Schema, fields


class HeartbeatResponseSchema(Schema):
    host = fields.Str(desciption='Hostname of the service.')
    status = fields.Str(description='Status of the service.')
