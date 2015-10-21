from django.conf.urls import url

from earth.views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^event/list$', events, name='events'),
]