
# Create your views here.

from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView
from .models import Link, Vote

class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

class AboutPageView(TemplateView):
    template_name = "about.html"

class SitesPageView(TemplateView):
    template_name = "sites.html"

class LinkListView(ListView):
    model = Link


