from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'example.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^gen_numbers/', 'simpleapi.views.numbers', name='gen_numbers'),
)
