from django.urls import path
from .views import *
'''
urlpatterns = [
    path('', IndexView.as_view(), name = 'index'),
    path('result/', result, name="result"),
]
'''

urlpatterns = [
    path('', index, name = 'index'),
    path('result/', result, name="result"),
]
