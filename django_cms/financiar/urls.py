from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^locations/$', views.locations_list, name='locations_list'),
    url(r'^location_new/$', views.location_new, name='location_new'),
    url(r'^location_edit/$', views.location_edit, name='location_edit'),
    url(r'^location_delete/$', views.location_delete, name='location_delete'),
    url(r'^salesdata/$', views.salesdata_list, name='salesdata_list'),
    url(r'^opens/$', views.opens_list, name='opens_list'),
    url(r'^traffic/$', views.traffic_list, name='traffic_list'),
    url(r'^indicators/$', views.indicators_list, name='indicators_list'),
    url(r'^trends/$', views.trends_list, name='trends_list'),
    url(r'^inflation/$', views.inflation_list, name='inflation_list'),
    url(r'^actions/$', views.actions_list, name='actions_list'),
    url(r'^finalsales/$', views.finalsales_list, name='finalsales_list'),
    url(r'^graffic/$', views.graffic_list, name='graffic_list'),]