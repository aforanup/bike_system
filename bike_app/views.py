from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from . forms import BikeForm
from django.urls import reverse_lazy
from . models import BikeModel, BikeImageModel
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView


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
    context_object_name = 'bike'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = BikeImageModel.objects.filter(
            bike=self.kwargs['pk']
        )
        return context


class DetailUpdateView(UpdateView):
    model = BikeModel
    template_name = 'bike_app/update.html'
    fields = ('name', 'description', 'image')
    context_object_name = 'bike'

    def get_success_url(self):
        return reverse_lazy('details', kwargs={'pk': self.object.id})


class BikeDeleteView(DeleteView):
    model = BikeModel
    template_name = 'bike_app/delete.html'
    success_url = reverse_lazy('home')


class BikeCreateView(CreateView, LoginRequiredMixin):
    template_name = 'bike_app/create.html'
    success_url = reverse_lazy('home')
    model = BikeModel
    fields = ('name', 'description', 'image')
