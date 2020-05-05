from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^projects$', views.projects),
    url(r'^lessons$', views.lessons),
    url(r'^about_us$', views.about_us),
    url(r'^news$', views.news)
]
