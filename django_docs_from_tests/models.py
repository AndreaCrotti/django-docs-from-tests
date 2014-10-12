import datetime

from django.db import models


class HttpCall(models.Model):
    content = models.TextField()
    headers = models.CharField(max_length=1024)

    class Meta:
        abstract = True


class Request(HttpCall):
    pass


class Response(HttpCall):
    status_code = models.IntegerField()


class ApiCall(models.Model):
    request = models.ForeignKey(Request)
    response = models.ForeignKey(Response)
    total_time = models.IntegerField()


class Query(models.Model):
    # TODO: should the queries be per-test or per API-call is enough?
    query = models.TextField()


class TestReportResult(models.Model):
    created = models.DateTimeField(default=datetime.datetime.utcnow)
    # TODO: queries should be a many to many?
    queries = models.ManyToManyField(Query)
    docstring = models.TextField(null=True, blank=True)
    name = models.CharField(max_length=128)
    calls = models.ManyToManyField(ApiCall)


