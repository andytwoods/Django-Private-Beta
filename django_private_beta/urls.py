from django.conf.urls import url
from . import views

app_name = 'private_beta'

urlpatterns = [
    url(r'^private_beta/', views.PrivateBeta.as_view(), name='private_beta'),
]
