from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^BookPerformer_profile', views.bookPerformer)
]
