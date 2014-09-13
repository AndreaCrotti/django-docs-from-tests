import logging
import os

from nose.plugins import Plugin

logger = logging.getLogger('nose.plugins.django_docs_from_tests')


class DocsFromTests(Plugin):
    name = 'helloworld'

    def options(self, parser, env=os.environ):
        super(DocsFromTests, self).options(parser, env=env)

    def configure(self, options, conf):
        super(DocsFromTests, self).configure(options, conf)
        if not self.enabled:
            return

    def finalize(self, result):
        logger.info('Hello pluginized world!')

