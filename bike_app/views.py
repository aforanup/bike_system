from django.shortcuts import render
from django.http import HttpResponse
from . models import BikeModel, BikeDetailModel, BikeImageModel
from django.views.generic import ListView


class BikeListView(ListView):
    model = BikeModel
    paginated_by = 4
    template_name = 'books/acme_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
