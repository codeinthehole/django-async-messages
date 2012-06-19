from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'tests.views.index'),
)
