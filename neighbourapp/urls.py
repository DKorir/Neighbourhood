from django.urls import path, include
from .views import HomeView,NeighbourDetailView
urlpatterns= [ 
    path('', HomeView.as_view(), name='home'),
    path('details/<int:pk>',NeighbourDetailView.as_view(), name='details'),
]