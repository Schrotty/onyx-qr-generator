from marshmallow import fields

from schema.request.GeneratorRequestSchema import GeneratorRequestSchema


class PersistenceRequestSchema(GeneratorRequestSchema):
    mime_type = fields.String(default='plain/text', required=True, desciption='The mime-type of the submitted payload.')
