from datetime import datetime
from django.shortcuts import render
from django.views import View
from jedzonko.models import Recipe
from random import shuffle

# doałem komentarz testowy

class IndexView(View):

    def get(self, request):
        ctx = {"actual_date": datetime.now()}
        return render(request, "test.html", ctx)


class MainView(View):

    def get(self, request):
        ctx = {}
        return render(request, 'dashboard.html', ctx)


class LandingPageView(View):

    def get(self, request):
        recipes = list(Recipe.objects.all())
        shuffle(recipes)
        ctx = {"recipes":recipes}
        return render(request, "index.html", ctx)


class RecipeAddView(View):
    def get(self, request):
        return render(request, 'app-add-recipe.html')
