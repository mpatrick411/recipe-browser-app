from django.urls import path
from . import views
from .views import home, view_recipes, add_recipe

urlpatterns = [
    path('', views.home, name='home'),
    path('view_recipes/', view_recipes, name='view_recipes'),
    path('add_recipe/', add_recipe, name='add_recipe'),
    path('delete_recipes/', views.delete_recipes, name='delete_recipes'),
]
