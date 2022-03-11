from marshmallow import Schema, fields


class PersistenceUpdateResponseSchema(Schema):
    identifier = fields.String(description='Result of the operation.')
    value = fields.Dict(keys=fields.String, values=fields.String)

