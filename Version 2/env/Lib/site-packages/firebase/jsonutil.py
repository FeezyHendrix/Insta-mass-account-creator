import datetime
import json
import decimal

try:
    total_seconds = datetime.timedelta.total_seconds
except AttributeError:
    total_seconds = lambda self: ((self.days * 86400 + self.seconds) * 10 ** 6 + self.microseconds) / 10 ** 6.0


class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime.datetime, datetime.date)):
            return obj.isoformat()
        elif isinstance(obj, datetime.timedelta):
            return total_seconds(obj)
        elif isinstance(obj, decimal.Decimal):
            return float(obj)
        else:
            return json.JSONEncoder.default(self, obj)
