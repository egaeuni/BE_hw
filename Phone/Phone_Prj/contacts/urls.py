from django.urls import path
from .views import *
from .views import IndexView

urlpatterns = [
    path('result/', result, name="result"),
    path('', IndexView.as_view(), name = 'index'),
]