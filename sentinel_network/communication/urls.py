from django.urls import path
from . import views

urlpatterns = [
    path("images/all/", views.ImageViewset.as_view(), name="all-images"), 
    
]