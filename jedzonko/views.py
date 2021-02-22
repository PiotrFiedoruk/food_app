from datetime import datetime
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpRequest, HttpResponse
from jedzonko.models import Recipe, Plan, RecipePlan
from random import shuffle
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView


# doałem komentarz testowy

class IndexView(View):

    def get(self, request):
        ctx = {"actual_date": datetime.now()}
        return render(request, "test.html", ctx)


class MainView(View):

    def get(self, request):
        total_recipes = Recipe.objects.all().count()
        ctx = {'total_recipes': total_recipes, }
        return render(request, 'dashboard.html', ctx)


class LandingPageView(View):

    def get(self, request):
        recipes = list(Recipe.objects.all())
        shuffle(recipes)
        total_recipes = Recipe.objects.all().count()
        ctx = {"recipes": recipes, 'total_recipes': total_recipes}
        return render(request, "index.html", ctx)

      
 # Recipe ------------------------------------------------

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


# Plans
class PlanListView(ListView):
    def get(self, request):
        all_plans = Plan.objects.all().order_by('name')
        page = request.GET.get('page', 1)
        paginator = Paginator(all_plans, 50)
        try:
            plans = paginator.page(page)
        except PageNotAnInteger:
            plans = paginator.page(1)
        except EmptyPage:
            plans = paginator.page(paginator.num_pages)
        ctx = {'plans': plans}
        return render(request, 'app-schedules.html', ctx)



class PlanDetailsView(View):
    def get(self, request):
        return render(request, 'app-details-schedules.html')


class PlanAddView(View):
    def get(self, request):
        return render(request, 'app-add-schedules.html')

    def post(self, request):
        plan_description = request.POST.get("planDescription")
        plan_name = request.POST.get("planName")
        err = ""
        if plan_description == "" or plan_name == "":
            error = "Proszę o wypełnienie obu pól"
            ctx = {'error': error}
            return render(request, 'app-add-schedules.html', ctx)
        else:
            new_plan = Plan(name=plan_name, description=plan_description)
            new_plan.save()
            new_plan_id = new_plan.id
        return redirect(f"plan/{new_plan_id}/details", )

class PlanAddRecipeView(View):
    def get(self, request):
        return render(request, 'app-add-schedules.html')
