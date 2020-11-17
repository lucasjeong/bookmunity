from django.conf.urls import url
from community import views

urlpatterns = [
    url(r'^about/$', views.AboutView.as_view(), name = 'about'),
]
