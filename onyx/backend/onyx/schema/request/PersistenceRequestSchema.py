from marshmallow import fields, validate

from onyx.schema.request.GeneratorRequestSchema import GeneratorRequestSchema


class PersistenceRequestSchema(GeneratorRequestSchema):
    mime_type = fields.String(default='plain/text', required=True, validate=validate.OneOf(['text/plain', 'image/png;base64', 'image/jpeg;base64']), desciption='The mime-type of the submitted payload.')
