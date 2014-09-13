import logging
import os

from nose.plugins import Plugin

logger = logging.getLogger('nose.plugins.helloworld')


class HelloWorld(Plugin):
    name = 'helloworld'

    def options(self, parser, env=os.environ):
        super(HelloWorld, self).options(parser, env=env)

    def configure(self, options, conf):
        super(HelloWorld, self).configure(options, conf)
        if not self.enabled:
            return

    def finalize(self, result):
        logger.info('Hello pluginized world!')
