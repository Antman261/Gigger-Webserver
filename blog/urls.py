from django.conf.urls import include, url
from django.contrib import admin
from . import views

app_name = 'blog'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name="blog-index"),
    url(r'^(?P<slug>[-\w]+)$', views.post, name='blog-post'),
]
