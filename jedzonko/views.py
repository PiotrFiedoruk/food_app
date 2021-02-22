from datetime import datetime

from django.shortcuts import render
from django.views import View

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
        return render(request, "index.html")

#Recipes

class RecipeAddView(View):
    def get(self, request):
        return render(request, 'app-add-recipe.html')

class RecipeDetails(View):
    def get(self, request):
        return render(request, 'app-recipe-details.html')

class RecipeListView(View):
    def get(self, request):
        return render(request, 'app-recipes.html')

class RecipeModifyView(View):
    def get(self, request):
        return render(request, 'app-edit-recipe.html')

#Plans

class PlanListView(View):
    def get(self, request):
        return render(request, 'app-schedules.html')

class PlanDetailsView(View):
    def get(self, request):
        return render(request, 'app-details-schedules.html')

class PlanAddView(View):
    def get(self, request):
        return render(request, 'app-add-schedules.html')

class PlanAddRecipeView(View):
    def get(self, request):
        return render(request, 'app-add-schedules.html')
