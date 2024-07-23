from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('form/', views.form_view, name='form_view'),
    path('form/<int:id>/', views.edit, name='edit'),  
    path('delete/<int:id>/', views.delete, name='delete'),
]