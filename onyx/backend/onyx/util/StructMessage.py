from datetime import datetime
import json


class StructMessage(object):
    def __init__(self, message, **kwargs):
        self.kwargs = kwargs
        self.kwargs['date'] = datetime.date(datetime.now()).__str__()
        self.kwargs['time'] = datetime.time(datetime.now()).__str__()
        self.kwargs['message'] = message

    def __str__(self):
        return json.dumps(self.kwargs)
