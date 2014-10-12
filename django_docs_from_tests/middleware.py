import inspect

from django_docs_from_tests import models


def find_test(stack_trace):
    for caller in stack_trace:
        if caller[3].startswith('test_'):
            return caller[0]


class RecordingRequestMiddleware(object):
    def process_response(self, request, response):
        test_stack = find_test(inspect.stack())
        request_db = models.Request.objects.create(
            path=request.path,
            method=request.META['REQUEST_METHOD'],
        )
        response_db = models.Response.objects.create(
            content=response.content,
            status_code=response.status_code,
        )
        models.ApiCall.objects.create(
            response=response_db,
            request=request_db,
            total_time=0.1,
        )
        
        return response
