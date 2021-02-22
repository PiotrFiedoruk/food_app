from datetime import datetime
<<<<<<< HEAD

from django.shortcuts import render, redirect
from django.views import View
from jedzonko.models import Recipe
from django.http import HttpRequest, HttpResponse
=======
from django.shortcuts import render
from django.views import View
from jedzonko.models import Recipe
from random import shuffle
>>>>>>> 68682a5687d08e86dd785ccd3e2754446cf32565

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

class RecipeDetails(View):
    def get(self, request):
        return render(request, 'app-recipe-details.html')

class RecipeListView(View):
    def get(self, request):
        return render(request, 'app-recipes.html')


    def post(self,request):
        ingr = request.POST.get("ingredients")
        prep_desc = request.POST.get("preparation_description")
        prep_time = int(request.POST.get("preparation_time"))
        recipe_desc = request.POST.get("recipe_description")
        recipe_name = request.POST.get("recipe_name")
        #
        #
        # return HttpResponse(f"{ingr}, {prep_desc}, {prep_time}, {recipe_desc}, {recipe_name}")
        if ingr != '' and prep_time != '' and prep_desc != '' and recipe_desc != '' and recipe_name != '':
            Recipe.objects.create(name=recipe_name, ingredients=ingr,preparation_time=prep_time, description=prep_desc, description_short=recipe_desc)
            return redirect('dashboard.html')
        else:
            return redirect('app-add-recipe.html')

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
