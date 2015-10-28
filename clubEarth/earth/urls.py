from django.conf.urls import url

from earth.views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^event/list$', events, name='events'),
    url(r'^news/list$', news, name='news'),
    url(r'^forums$', forums, name='forums'),
]