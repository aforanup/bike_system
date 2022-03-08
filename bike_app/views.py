from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from . forms import BikeForm
from django.urls import reverse_lazy
from . models import BikeModel, BikeDetailModel, BikeImageModel
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, TemplateView


class BikeListView(ListView):
    model = BikeModel
    paginated_by = 5
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
    template_name = 'bike_app/home.html'


class BikeDeleteView(DeleteView):
    model = BikeModel
    template_name = 'bike_app/delete.html'
    success_url = reverse_lazy('home')


class BikeCreateView(TemplateView):
    template_name = 'bike_app/create.html'
    success_url = reverse_lazy('home')

    def get(self):
        pass
