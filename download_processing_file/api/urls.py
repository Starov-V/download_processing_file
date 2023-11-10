from django.urls import include, path
from rest_framework import routers
from .views import FileList


urlpatterns = [
    path('upload/', FileList().as_view(http_method_names=['post'])),
    path('files/', FileList().as_view(http_method_names=['get'])),
]