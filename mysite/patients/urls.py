from django.conf.urls import url

from . import views

app_name = 'patients'
urlpatterns = [
	# /patients/
    url(r'^$', views.index, name='index'),
    # /patients/5/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
]