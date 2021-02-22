from datetime import datetime

from django.shortcuts import render, redirect
from django.views import View
from jedzonko.models import Recipe
from django.http import HttpRequest, HttpResponse

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

class RecipeAddView(View):
    def get(self,request):
        return render(request,'app-add-recipe.html')

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
