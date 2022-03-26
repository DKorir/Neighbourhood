from django.urls import path, include
from .views import HomeView,NeighbourDetailView,AddPostview
urlpatterns= [ 
    path('', HomeView.as_view(), name='home'),
    path('details/<int:pk>',NeighbourDetailView.as_view(), name='details'),
    path('add_post/',AddPostview.as_view(),name='add_post'),
   
]