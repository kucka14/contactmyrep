from django.urls import path
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('robots.txt', views.robots, name='robots'),
	path('sitemap.xml', views.sitemap, name='sitemap')
]


