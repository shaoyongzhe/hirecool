from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ApiEndpoint.as_view(), name='shaoyz'),
]