from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^locations/$', views.locations_list, name='locations_list'),
    url(r'^salesdata/$', views.salesdata_list, name='salesdata_list'),
    url(r'^opens/$', views.opens_list, name='opens_list'),
    url(r'^traffic/$', views.traffic_list, name='traffic_list'),
    url(r'^indicators/$', views.indicators_list, name='indicators_list'),
    url(r'^trends/$', views.trends_list, name='trends_list'),
    url(r'^inflation/$', views.inflation_list, name='inflation_list'),
    url(r'^actions/$', views.actions_list, name='actions_list'),
]