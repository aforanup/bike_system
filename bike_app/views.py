from django.shortcuts import render
from django.http import HttpResponse
from . models import BikeModel, BikeDetailModel, BikeImageModel
from django.views.generic import ListView, DetailView


class BikeListView(ListView):
    model = BikeModel
    paginated_by = 4
    template_name = 'bike_app/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bikes'] = BikeModel.objects.all()
        return context


class BikeDetailView(DetailView):
    model = BikeDetailModel
    template_name = 'bike_app/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['details'] = bikeDetailModel.objects.filter(
            pk=self.kwargs['pk']
        )
        return context
