from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^FAQ', views.faq),
    url(r'^About', views.about),
    url(r'^Contact', views.contact),
    url(r'^Privacy', views.privacy),
    url(r'^TermsAndConditions', views.tos),
    url(r'^.*$', views.catchall, name='catch-all')
]
