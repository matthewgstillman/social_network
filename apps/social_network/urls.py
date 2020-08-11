from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^register$', views.register, name="register"),
    url(r'^landing$', views.landing, name="landing"),
    url(r'^login$', views.login, name="login"),
]