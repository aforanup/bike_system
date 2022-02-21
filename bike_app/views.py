from django.shortcuts import render
from django.http import HttpResponse
from . models import BikeModel, BikeDetailModel, BikeImageModel
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView


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
        print("aaa", self.kwargs['pk'])
        context['details'] = BikeDetailModel.objects.get(
            bike=int(self.kwargs['pk'])
        )
        context['images'] = BikeImageModel.objects.filter(
            bike_model=int(self.kwargs['pk'])
        )
        print(context['details'], 'bbbb')
        return context


class DetailUpdateView(UpdateView):
    model = BikeModel
    paginated_by = 4
    template_name = 'bike_app/home.html'


class BikeDeleteView(DeleteView):
    model = BikeModel
    paginated_by = 4
    template_name = 'bike_app/home.html'


class BikeCreateView(CreateView):
    model = BikeModel
    paginated_by = 4
    template_name = 'bike_app/home.html'
