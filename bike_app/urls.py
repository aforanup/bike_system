from django.urls import path, include
from . import views

urlpatterns = [
    path('', include([
        path('', views.BikeListView.as_view(), name="home"),
        path('<str:pk>/', views.BikeDetailView.as_view(), name="details"),
    ])),
    path('create/', views.BikeCreateView.as_view(), name="create"),
]
