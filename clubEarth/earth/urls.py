from django.conf.urls import url

from earth.views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^home$', home, name='home'),
    url(r'^event/list$', events, name='events'),
    url(r'^event/(?P<event_id>\d+)$', event_info, name="event_info"),
    url(r'^news/list$', news, name='news'),
    url(r'^forums$', forums, name='forums'),
]