from django.contrib import admin
from django.urls import path, include
from cadVeiculos.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',  include('cadVeiculos.urls'))

]
