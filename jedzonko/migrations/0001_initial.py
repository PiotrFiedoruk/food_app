# Generated by Django 2.2.6 on 2021-02-22 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DayName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('order', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('created', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('ingredients', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('created', models.DateField(auto_now=True)),
                ('updated', models.DateField(auto_now=True)),
                ('preparation_time', models.IntegerField()),
                ('votes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='RecipePlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meal_name', models.CharField(max_length=64)),
                ('order', models.IntegerField()),
                ('day_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jedzonko.DayName')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jedzonko.Plan')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jedzonko.Recipe')),
            ],
        ),
        migrations.AddField(
            model_name='plan',
            name='recipe',
            field=models.ManyToManyField(through='jedzonko.RecipePlan', to='jedzonko.Recipe'),
        ),
    ]
