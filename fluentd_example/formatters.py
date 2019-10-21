import fluent.handler

class StringFluentRecordFormatter(fluent.handler.FluentRecordFormatter):
    """ Formats FluentRecordFormatter dict to a string.
    """
    def format(self, record):
        fmtd_dict = super(StringFluentRecordFormatter, self).format(record)
        return str(fmtd_dict)
