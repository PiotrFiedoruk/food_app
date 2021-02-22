"""scrumlab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path


from jedzonko.views import IndexView, LandingPageView, MainView, RecipeAddView, RecipeDetails, RecipeListView, \
    RecipeAddView, RecipeModifyView, PlanDetailsView, PlanAddView, PlanAddRecipeView, PlanListView

urlpatterns = [
    path("", LandingPageView.as_view(), name="landing_page"),
    path('index/', IndexView.as_view(), name="index"),
    path('main/', MainView.as_view(), name="main"),
    #Recipes
    path('recipe/add/', RecipeAddView.as_view(), name="recipe_add"),
    path('recipe/<int:id>/', RecipeDetails.as_view(), name='recipe_details'),
    path('recipe/list/', RecipeListView.as_view(), name='recipe_list'),
    path('recipe/modify/<int:id>/', RecipeModifyView.as_view(), name='recipe_modify'),
    # Plans
    path('plan/list/', PlanListView.as_view(), name='plan_list'),
    path('plan/<int:id>/', PlanDetailsView.as_view(), name='plan_details'),
    path('plan/add/', PlanAddView.as_view(), name='plan_add'),
    path('plan/add-recipe/', PlanAddRecipeView.as_view(), name='plan_add_recipe'),
    path('admin/', admin.site.urls),

]
