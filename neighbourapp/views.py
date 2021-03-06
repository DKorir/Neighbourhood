from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView,CreateView

from neighbourapp.models import Neighbourhood, Post


class HomeView(ListView):
    model=Post
    template_name='home.html'
class NeighbourDetailView(DetailView):
    model=Post
    template_name='details.html'

class AddPostview(CreateView):
    model=Post
    template_name='add_post.html'
    fields='__all__'



