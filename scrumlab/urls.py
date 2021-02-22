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


from jedzonko.views import IndexView, LandingPageView, MainView, RecipeAddView, RecipeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', IndexView.as_view(), name="index"),
    path('main/', MainView.as_view(), name="main"),
    path("", LandingPageView.as_view(), name="landing_page"),
    path('recipe/add', RecipeAddView.as_view()),
    path('recipe/<int:id>', RecipeView.as_view(), name='view_recipe'),


]
