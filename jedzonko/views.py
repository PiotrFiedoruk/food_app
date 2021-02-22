from datetime import datetime
from django.shortcuts import render, redirect
from django.views import View
from jedzonko.models import Recipe
from django.http import HttpRequest, HttpResponse
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



class RecipeDetails(View):
    def get(self, request):
        return render(request, 'app-recipe-details.html')

class RecipeListView(View):
    def get(self, request):
        return render(request, 'app-recipes.html')

class RecipeAddView(View):
    def get(self, request):
        error = request.GET.get("error")
        return render(request, 'app-add-recipe.html')

    def post(self,request):
        ingr = request.POST.get("ingredients")
        prep_desc = request.POST.get("preparation_description")
        prep_time = request.POST.get("preparation_time")
        recipe_desc = request.POST.get("recipe_description")
        recipe_name = request.POST.get("recipe_name")
        if ingr != '' and prep_time != '' and prep_desc != '' and recipe_desc != '' and recipe_name != '':
            Recipe.objects.create(name=recipe_name, ingredients=ingr,preparation_time=int(prep_time), description=prep_desc, description_short=recipe_desc)
            return redirect('recipe_list')
        else:
            error = "Wypełnij prawidłowo wszystkie pola"
            return render(request,'app-add-recipe.html', {"error": error})

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
