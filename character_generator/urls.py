from django.contrib import admin
from django.urls import path
from name_generator import views
from django.urls import path, include



urlpatterns = [
    path('generate_name/', views.generate_name, name='generate_name'),
    path('admin/', admin.site.urls),
    path('name_generator/', include('name_generator.urls')),
]
