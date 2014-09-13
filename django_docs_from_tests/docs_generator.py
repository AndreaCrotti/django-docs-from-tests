

class TestResult(object):
    def __init__(self, test_name, docs=None):
        self.test_name = test_name

    def render(self):
        return '<div id="{0}"> {0} </div>'.format(self.test_name)
