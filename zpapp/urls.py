from django.conf.urls import url
from zpapp.views import home, add_worker, acts


urlpatterns = [
    url(r'^$',home, name='home'),
    url(r'^add/$',add_worker, name='add'),
    url(r'^act/(?P<obj>[0-9&]+)$',acts, name='act')
]