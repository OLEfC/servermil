# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.esp_data, name='esp_data'),
    #path('view_data', views.view_data, name='view_data'),

]
