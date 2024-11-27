from django.urls import path
from . import views

urlpatterns = [
    path('get_results/', views.get_results, name='get_results'),
]