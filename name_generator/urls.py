from django.urls import path
from . import views

urlpatterns = [
    path('generate_name/', views.generate_name, name='generate_name'),
    # Add other URL patterns as needed
]
