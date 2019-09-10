import json
from . import GOIPStatus
class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, GOIPStatus.GOIPData):
            return obj.getJSONObj()
        if isinstance(obj, GOIPStatus.GOIPDataHeader):
            return obj.getJSONObj()
        if isinstance(obj, GOIPStatus.GPIOPin):
            return obj.getJSONObj()
        return json.JSONEncoder.default(self, obj)