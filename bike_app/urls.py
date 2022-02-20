from django.urls import path, include
from . import views

urlpatterns = [
    path('', include([
        path('', views.BikeListView.as_view(), name="home"),
        path('details/', views.BikeDetailView.as_view(), name="details")
    ]))
]
