from django.urls.conf import path
from app2.views import *
app_name='app2'
urlpatterns = [
    path('nani4/',nani4,name='nani4'),
]