from django.shortcuts import render
from django.http import Http404
from . forms import BikeForm
from . models import BikeModel, BikeDetailModel, BikeImageModel
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, FormView


class BikeListView(ListView):
    model = BikeModel
    paginated_by = 4
    template_name = 'bike_app/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bikes'] = BikeModel.objects.all()
        return context


class BikeDetailView(DetailView):
    model = BikeModel
    template_name = 'bike_app/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['details'] = BikeDetailModel.objects.get(
            bike=self.kwargs['pk']
        )
        context['images'] = BikeImageModel.objects.filter(
            bike=self.kwargs['pk']
        )
        return context


class DetailUpdateView(UpdateView):
    model = BikeModel
    paginated_by = 4
    template_name = 'bike_app/home.html'


class BikeDeleteView(DeleteView):
    model = BikeModel
    template_name = 'bike_app/home.html'


class BikeCreateView(FormView):
    form_class = BikeForm
    template_name = 'bike_app/create.html'
    success_url = 'home'
