from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^salesdata/$', views.salesdata_list, name='salesdata_list'),
]