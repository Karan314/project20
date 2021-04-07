from app2 import views
from django.urls import path
app_name="app2"

urlpatterns = [
    path('<data>/',views.ind,name="index1"),
    path('sample2/',views.sample,name="sample1"),
    path('temp2/',views.temp2,name="temp2"),
]
