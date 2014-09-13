import json

from django.test import TestCase
from django.core.urlresolvers import reverse

# Create your tests here.


class TestSimpleApi(TestCase):
    def test_getting_numbers_returns_list_of_first_numbers(self):
        url = reverse('gen_numbers')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(data, list(range(10)))
