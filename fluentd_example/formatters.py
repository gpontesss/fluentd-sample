import json

import fluent.handler


class StringFluentRecordFormatter(fluent.handler.FluentRecordFormatter):
    """ Formats FluentRecordFormatter dict to a string.
    """

    def format(self, record):
        fmtd_dict = super(StringFluentRecordFormatter, self).format(record)
        return json.dumps(fmtd_dict)
