from django.urls import path
from recognization import views

app_name = 'recognization'
urlpatterns = [
    path('api/images/', views.api_images, name="api_images"),
    path('', views.index, name="index")
]
