from django.test import TestCase

# Create your tests here.

from django_docs_from_tests import models


class ResponseTest(TestCase):
    def test_create_response(self):
        resp = models.Response.objects.create(content='hello', status_code=202, headers={})
        req = models.Request.objects.create(content='hello', headers={})
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
