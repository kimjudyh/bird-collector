from django.urls import path
from . import views

urlpatterns = [
    # root route
    path('', views.home, name='home'),
    # birds index view
    path('birds/', views.birds_index, name='index'),
    # birds detail view
    path('birds/<int:bird_id>/', views.birds_detail, name='detail'),
    # birds new view
    path('birds/new/', views.new_bird, name='new_bird'),
    # new sighting view
    path('birds/<int:bird_id>/new_sighting/', views.new_sighting, name='new_sighting'),
    # associate/remove association between bird, nest material
    path('birds/<int:bird_id>/assoc_nest/<int:nest_material_id>/', views.assoc_nest, name='assoc_nest'),
]