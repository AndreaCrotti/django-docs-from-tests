from django.core.urlresolvers import reverse
from django.test import TestCase

# Create your tests here.

from django_docs_from_tests import models


class ModelsTest(TestCase):
    def test_models(self):
        resp = models.Response.objects.create(content='hello', status_code=202, headers={})
        req = models.Request.objects.create(path='/hello')
        api_call = models.ApiCall.objects.create(request=req, response=resp, total_time=0.1)

        query = models.Query.objects.create(query='select * from jonny;')
        # TODO: now create the query object
        result = models.TestReportResult.objects.create(
            docstring="Hello docstring",
            name="test_hello_world",
        )
        result.queries.add(query)
        result.calls.add(api_call)

        self.assertEqual(result.calls.first().request, req)
        self.assertEqual(result.calls.first().response, resp)


class MiddlewareRecordingTest(TestCase):
    def test_find_test_caller(self):
        from django_docs_from_tests.middleware import find_test
        sampl = [('trace', 100, 'file', 'func'), ('tr', 10, 'file', 'test_hello_world')]
        # just return the object
        self.assertEqual(find_test(sampl), 'tr')

    def test_getting_numbers_returns_list_of_first_numbers(self):
        url = reverse('gen_numbers')

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        # this should have added some stuff in the database as a side effect
        self.assertEqual(models.ApiCall.objects.count(), 1)
        call = models.ApiCall.objects.first()
        self.assertEqual(call.response.status_code, 200)
