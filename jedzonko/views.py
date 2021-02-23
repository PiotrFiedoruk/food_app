from datetime import datetime
from django.shortcuts import render
from django.views import View
from jedzonko.models import Recipe, Plan, DayName, RecipePlan, Page
from random import shuffle


# doałem komentarz testowy

class IndexView(View):

    def get(self, request):
        ctx = {"actual_date": datetime.now()}
        return render(request, "test.html", ctx)


class MainView(View):

    def get(self, request):
        plans_sorted = Plan.objects.all().order_by("-created")
        newest_plan = plans_sorted[0]
        pn = newest_plan.recipeplan_set.filter(day_name=(DayName.objects.get(name='poniedziałek')))
        wt = newest_plan.recipeplan_set.filter(day_name=(DayName.objects.get(name='wtorek')))
        sr = newest_plan.recipeplan_set.filter(day_name=(DayName.objects.get(name='środa')))
        cz = newest_plan.recipeplan_set.filter(day_name=(DayName.objects.get(name='czwartek')))
        pt = newest_plan.recipeplan_set.filter(day_name=(DayName.objects.get(name='piątek')))
        so = newest_plan.recipeplan_set.filter(day_name=(DayName.objects.get(name='sobota')))
        nd = newest_plan.recipeplan_set.filter(day_name=(DayName.objects.get(name='niedziela')))
        print(pn[1].day_name.name)
        ctx = {
            'number_of_plans': Plan.objects.count(),
            'newest_plan': plans_sorted[0],
            'recipeplan_per_days': [pn, wt, sr, cz, pt, so, nd]
        }
        return render(request, 'dashboard.html', ctx)


class LandingPageView(View):

    def get(self, request):
        recipes = list(Recipe.objects.all())
        shuffle(recipes)
        ctx = {"recipes": recipes}
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


class RecipeModifyView(View):
    def get(self, request):
        return render(request, 'app-edit-recipe.html')


# Plans

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
