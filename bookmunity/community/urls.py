from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^main/$', views.MainView.as_view(), name = 'main'),
    url(r'^search/$', views.SearchView.as_view(), name = 'search'),
    url(r'^search/(?P<pk>\d+)$', views.SearchView.as_view(), name = 'search'),

]
