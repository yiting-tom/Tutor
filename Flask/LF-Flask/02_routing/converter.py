
class RegexConverter(BaseConverter):
    r"""The Regex Converter class.

    Parameters
    ==========
    map : str
        The
    """

    def __init__(self):
        super(RegexConverter, self).__init__(map)
        self.regex = regex

    @staticmethod
    def to_python(value):
        r"""Transform the regex pattern into python data type."""
        return value

    def to_url(self, value):
        r"""When using url_for() to get url, return the params for the url."""
        return super(RegexConverter, self).to_url(value)