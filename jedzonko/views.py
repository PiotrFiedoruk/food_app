from datetime import datetime

from django.shortcuts import render
from django.views import View

# doałem komentarz testowy

class IndexView(View):

    def get(self, request):
        ctx = {"actual_date": datetime.now()}
        return render(request, "test.html", ctx)
