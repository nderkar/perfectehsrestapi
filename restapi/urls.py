from django.urls import path, include
from rest_framework import  routers
from  . import views

routers = routers.DefaultRouter()
routers.register(r'employer', views.EmployerViewset)
urlpatterns = [
    path('', include(routers.urls)),
    path('api_auth/', include('rest_framework.urls', namespace='rest_framework'))
]