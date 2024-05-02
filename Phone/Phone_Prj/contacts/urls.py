from django.urls import path
from .views import list, create, detail, update, delete

'''
urlpatterns = [
    path('', IndexView.as_view(), name = 'index'),
    path('result/', result, name="result"),
]
'''

urlpatterns = [
    path('', list, name = 'list'),
    #path('result/', result, name="result"),
    path('create/', create, name = "create"),
    path('detail/<int:id>/', detail, name="detail"),
    path('update/<int:id>/', update, name="update"),
    path('delete/<int:id>/', delete, name="delete"),
]



