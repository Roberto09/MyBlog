from django.conf.urls import url, include
from apps.Home.views import HomeScreen, AboutMe, Academic

urlpatterns = [
    url(r'^$', HomeScreen, name='HomeScreen'),
    url(r'^AboutMe$', AboutMe, name='AboutMe'),
    url(r'^Academic$', Academic, name='Academic'),
]