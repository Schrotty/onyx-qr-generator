from marshmallow import Schema, fields


class PersistenceUpdateRequestSchema(Schema):
    value = fields.String(required=True, description='The payload to persist.')
    mime_type = fields.String(default='plain/text', required=True, desciption='The mime-type of the submitted payload.')
