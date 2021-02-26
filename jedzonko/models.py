from django.db import models
from django.template.defaultfilters import slugify


class Recipe(models.Model):
    name = models.CharField(max_length=64)
    ingredients = models.CharField(max_length=255)
    description = models.TextField()
    created = models.DateField(auto_now=True)
    updated = models.DateField(auto_now=True)
    preparation_time = models.IntegerField()
    votes = models.IntegerField(default=0)
    description_short = models.CharField(max_length=128)



class Plan(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    created = models.DateField(auto_now=True)
    recipe = models.ManyToManyField(Recipe, through='RecipePlan')


class DayName(models.Model):
    name = models.CharField(max_length=25)
    order = models.IntegerField()


class RecipePlan(models.Model):
    meal_name = models.CharField(max_length=64)
    order = models.IntegerField()
    day_name = models.ForeignKey(DayName, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)

    class Meta:
        ordering = ('order',)


class Page(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Page, self).save(*args, **kwargs)



