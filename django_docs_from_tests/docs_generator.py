HTML_PREAMBLE = """"
<html><head>
<title>Test output</title>
</head><body>
"""

HTML_CLOSING = """
</body>
</html>
"""


class Report(object):
    def __init__(self, name, description=None):
        self.name = name
        self.description = description
        self.tests = []

    def add(self, test):
        self.tests.append(test)

    @property
    def body(self):
        return '\n'.join(test.render() for test in self.tests)

    def render(self):
        return "{}{}{}".format(HTML_PREAMBLE, self.body, HTML_CLOSING)


class TestResult(object):
    def __init__(self, test_name, docs=None):
        self.test_name = test_name

    def render(self):
        return '<div id="{0}"> {0} </div>'.format(self.test_name)
