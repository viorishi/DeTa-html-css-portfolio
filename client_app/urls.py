from django.urls import path
from app.views import index

from .views import index, create_employee

urlpatterns = [
    path('', index, name="client.index"),
    path('create_employee/<name>', create_employee, name="create_employee")
]    