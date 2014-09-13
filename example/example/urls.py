from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^gen_numbers/', 'simpleapi.views.numbers', name='gen_numbers'),
)
