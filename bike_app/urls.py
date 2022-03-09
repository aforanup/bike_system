from django.urls import path, include
from . import views

urlpatterns = [
    path('', include([
        path('', views.BikeListView.as_view(), name="home"),
        path('<int:pk>/', views.BikeDetailView.as_view(), name="details"),
        path('<int:pk>/delete/', views.BikeDeleteView.as_view(), name="delete"),
        path('<int:pk>/update', views.DetailUpdateView.as_view(), name="update"),
    ])),
    path('create/', views.BikeCreateView.as_view(), name="create"),
]
