from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	# url(r'^hoara/(?P<ticker>[A-Z]{1,5})', views.hoara, name='hoara')
]
