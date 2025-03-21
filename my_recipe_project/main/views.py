from django.http import HttpResponse
from .models import Recipe
from .forms import RecipeForm
from django.shortcuts import render, redirect

# Home landing page
def home(request):
    return render(request, 'main/home.html')

# Retrieves and displays all recipes from the database. Also contains my logic for searching/filtering
def view_recipes(request): 
    search_query = request.GET.get('search_query', '').strip()

    if search_query:
        recipes = Recipe.objects.filter(
            name__icontains = search_query
        ) | Recipe.objects.filter(
            ingredients__icontains = search_query
        )
    else:
        recipes=Recipe.objects.all()


    return render(request, 'main/view_recipes.html', {'recipes': recipes, 'search_query': search_query})

# Handles adding a new recipe
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_recipes')
    else:
        form = RecipeForm()

    return render(request, 'main/add_recipe.html', {'form': form})

# Handles deleting selected recipes on the view_recipes template screen
def delete_recipes(request):
    if request.method == 'POST':
        recipe_ids = request.POST.getlist('recipes_to_delete')
        Recipe.objects.filter(id__in=recipe_ids).delete()
    return redirect('view_recipes')


