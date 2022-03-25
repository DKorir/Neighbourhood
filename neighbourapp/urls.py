from django.urls import path, include
from .views import HomeView,NeighbourDetailView,AddPostview,AddBusinessview
urlpatterns= [ 
    path('', HomeView.as_view(), name='home'),
    path('details/<int:pk>',NeighbourDetailView.as_view(), name='details'),
    path('add_post/',AddPostview.as_view(),name='add_post'),
    path('add_business/',AddBusinessview.as_view(),name='add_business'),
]