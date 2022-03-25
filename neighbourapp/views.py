from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView

from neighbourapp.models import Neighbourhood


class HomeView(ListView):
    model=Neighbourhood
    template_name='home.html'
class NeighbourDetailView(DetailView):
    model=Neighbourhood
    template_name='details.html'
