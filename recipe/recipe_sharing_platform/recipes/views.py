from django.http import JsonResponse, HttpResponseBadRequest
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import LoginForm, RegistrationForm, RecipeForm
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import Recipe, Rating, Comment, Category, Ingredient
import json

# GET Endpoints
def get_all_recipes(request):
    recipes = Recipe.objects.all()
    data = []
    for recipe in recipes:
        recipe_data = {
            'id': recipe.id,
            'title': recipe.title,
            'author': recipe.author.username,
            'category': recipe.category.name,
            'ingredients': [ingredient.name for ingredient in recipe.ingredients.all()]  # Extract ingredients
        }
        data.append(recipe_data)
    return JsonResponse(data, safe=False)

def get_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    data = {
        'id': recipe.id,
        'title': recipe.title,
        'author': recipe.author.username,
        'category': recipe.category.name,
        'ingredients': [ingredient.name for ingredient in recipe.ingredients.all()]  # Extract ingredients
    }
    return JsonResponse(data)

def get_recipes_by_category(request, category_id):
    recipes = Recipe.objects.filter(category=category_id)
    data = [{'id': recipe.id, 'title': recipe.title, 'author': recipe.author.username, 'category': recipe.category.name} for recipe in recipes]
    return JsonResponse(data, safe=False)

def get_all_ratings(request):
    ratings = Rating.objects.all()
    data = [{'id': rating.id, 'recipe_id': rating.recipe.id, 'user': rating.user.username, 'rating': rating.rating} for rating in ratings]
    return JsonResponse(data, safe=False)

def get_ratings_for_recipe(request, recipe_id):
    ratings = Rating.objects.filter(recipe_id=recipe_id)
    data = [{'id': rating.id, 'user': rating.user.username, 'rating': rating.rating} for rating in ratings]
    return JsonResponse(data, safe=False)

def get_comments_for_recipe(request, recipe_id):
    comments = Comment.objects.filter(recipe_id=recipe_id)
    data = [{'id': comment.id, 'user': comment.user.username, 'text': comment.text} for comment in comments]
    return JsonResponse(data, safe=False)

#POST endpoints
@csrf_exempt
@login_required
def create_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            author = request.user
            category = form.cleaned_data['category']
            ingredients = form.cleaned_data['ingredients']
            instructions = form.cleaned_data['instructions']

            recipe = Recipe.objects.create(title=title, author=author, category=category, instructions=instructions)
            recipe = Recipe.objects.create(title=title, author=author, category=category, instructions=instructions)

            # Clear existing ingredients and add new ones
            recipe.ingredients.clear()  # Clear existing ingredients
            recipe.ingredients.add(*ingredients)  # Add new ingredients
            return JsonResponse({'id': recipe.id, 'message': 'Recipe created successfully'})
        else:
            return HttpResponseBadRequest("Invalid data. Please check your input.")
    else:
        form = RecipeForm()
        return render(request, 'recipe_form.html', {'form': form})

@csrf_exempt
@login_required
def rate_recipe(request, recipe_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        rating_value = data.get('rating')
        if not rating_value:
            return HttpResponseBadRequest("Rating value is required")
        user = request.user
        recipe = get_object_or_404(Recipe, pk=recipe_id)
        rating, created = Rating.objects.get_or_create(recipe=recipe, user=user)
        rating.rating = rating_value
        rating.save()
        return JsonResponse({'id': rating.id, 'message': 'Rating updated successfully'})

@csrf_exempt
@login_required
def add_comment(request, recipe_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        text = data.get('text')
        if not text:
            return HttpResponseBadRequest("Comment text is required")
        user = request.user
        recipe = get_object_or_404(Recipe, pk=recipe_id)
        comment = Comment.objects.create(recipe=recipe, user=user, text=text)
        return JsonResponse({'id': comment.id, 'message': 'Comment added successfully'})

@csrf_exempt
@login_required
def leave_comment(request, recipe_id):
    if request.method == 'POST':
        text = request.POST.get('text')
        if not text:
            return HttpResponseBadRequest("Comment text is required")
        user = request.user
        recipe = Recipe.objects.get(pk=recipe_id)
        comment = Comment.objects.create(recipe=recipe, user=user, text=text)
        return JsonResponse({'id': comment.id, 'message': 'Comment added successfully'})

@csrf_exempt
def create_category(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        if not name:
            return HttpResponseBadRequest("Category name is required")
        category = Category.objects.create(name=name)
        return JsonResponse({'id': category.id, 'name': category.name, 'message': 'Category created successfully'})
    else:
        return HttpResponseNotAllowed(['POST'])

@csrf_exempt
def create_ingredient(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        if not name:
            return HttpResponseBadRequest("Ingredient name is required")
        ingredient = Ingredient.objects.create(name=name)
        return JsonResponse({'id': ingredient.id, 'name': ingredient.name, 'message': 'Ingredient created successfully'})
    else:
        return HttpResponseNotAllowed(['POST'])
    
@csrf_exempt
@login_required
def update_user_info(request):
    if request.method == 'POST':
        user = request.user
        data = request.POST
        # Update user information
        if 'username' in data:
            user.username = data['username']
        if 'email' in data:
            user.email = data['email']
        user.save()
        return JsonResponse({'message': 'User information updated successfully'})

@csrf_exempt
@login_required
def update_recipe_info(request, recipe_id):
    if request.method == 'POST':
        recipe = Recipe.objects.get(pk=recipe_id)
        data = request.POST
        # Update recipe information
        if 'title' in data:
            recipe.title = data['title']
        if 'category_id' in data:
            recipe.category_id = data['category_id']
        if 'ingredients' in data:
            ingredients = data.getlist('ingredients')
            recipe.ingredients.clear()
            recipe.ingredients.add(*ingredients)
        if 'instructions' in data:
            recipe.instructions = data['instructions']
        recipe.save()
        return JsonResponse({'message': 'Recipe information updated successfully'})

#Auth
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('recipes')  # Redirect to the home page after successful login
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to the login page after successful registration
    else:
        form = RegistrationForm()
    return render(request, 'registration.html', {'form': form})
