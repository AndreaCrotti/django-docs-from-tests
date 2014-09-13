import logging
import os

from nose.plugins import Plugin

logger = logging.getLogger('nose.plugins.django_docs_from_tests')


class DocsFromTests(Plugin):
    name = 'docs-from-tests'

    def __init__(self):
        super(DocsFromTests, self).__init__()
        # self.html = [ '<html><head>',
        #               '<title>Test output</title>',
        #               '</head><body>' ]

    def options(self, parser, env=os.environ):
        super(DocsFromTests, self).options(parser, env=env)

    def configure(self, options, conf):
        super(DocsFromTests, self).configure(options, conf)
        if not self.enabled:
            return

        # TODO: might need to intercept some calls done in the client
        # to make sure things get executed correctly

    def finalize(self, result):
        logger.info('Hello pluginized world!')

