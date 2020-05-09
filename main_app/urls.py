from django.urls import path
from . import views

urlpatterns = [
    # root route
    path('', views.home, name='home'),
    # birds index view
    path('birds/', views.birds_index, name='index'),
    # birds detail view
    path('birds/<int:bird_id>/', views.birds_detail, name='detail'),
]