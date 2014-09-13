import json
from mock import patch

from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client


class DebuggingClient(Client):
    def __init__(self, *args, **kwargs):
        super(DebuggingClient, self).__init__(*args, **kwargs)

    def get(self, url, *args, **kwargs):
        print("Calling endpoint {} with args {} and kwargs {}".format(url, args, kwargs))
        response = super(DebuggingClient, self).get(url, *args, **kwargs)
        print("Obtained response {}:{}".format(response.status_code, response.content))
        return response


class TestSimpleApi(TestCase):
    # TODO: how do I make this happen inside the plugin??
    def _pre_setup(self):
        super(TestSimpleApi, self)._pre_setup()
        self.client = DebuggingClient()

    def test_getting_numbers_returns_list_of_first_numbers(self):
        url = reverse('gen_numbers')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(data, list(range(10)))
