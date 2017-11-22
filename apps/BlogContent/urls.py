from django.conf.urls import url, include
from apps.BlogContent.views import SeeBP

urlpatterns = [
    url(r'^MyBlogs', SeeBP.as_view() , name='see_BP'),
]