from django.urls import path
from .views import checkout,detail

urlpatterns = [
    path('',checkout,name='checkout'),
    path('detail/',detail,name='detail')
]