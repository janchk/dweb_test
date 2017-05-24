from django.conf.urls import url
from app_test.views import rqst_hndlr, stat_view
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^rqst_hndlr', rqst_hndlr, name='rqst_hndlr'),
    url(r'stat_view', stat_view, name='stat_view'),
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^statistics', TemplateView.as_view(template_name='statistics.html'), name='statistics')
]
