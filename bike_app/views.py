from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.db.models import Q
from . forms import BikeImageForm, BikeForm
from django.urls import reverse_lazy
from . models import BikeModel, BikeImageModel
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView, View, TemplateView


class BikeListView(TemplateView):
    # paginated_by = 5
    template_name = 'bike_app/home.html'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        query = request.GET.get('search') if request.GET.get(
            'search') != None else ''
        context['bikes'] = BikeModel.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
        return render(request, self.template_name, context)


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


# def AddImages(request):
#     form = BikeImageForm()
#     if request.method == 'POST':
#     else:
#         return render(request, '')


class BikeDeleteView(DeleteView):
    model = BikeModel
    template_name = 'bike_app/delete.html'
    success_url = reverse_lazy('home')


class BikeCreateView(View):
    template_name = 'bike_app/create.html'

    def get(self, request):
        bike_form = BikeForm
        bike_image_form = BikeImageForm
        return render(request, self.template_name, context={"page": "create", "bike_form": bike_form, "bike_image_form": bike_image_form})

    def post(self, request):
        bike_form = BikeForm(request.POST, request.FILES)
        bike_image_form = BikeImageForm(request.POST, request.FILES)
        if bike_form.is_valid() and bike_image_form.is_valid():
            bike = bike_form.save(commit=False)
            bike.user = request.user
            bike.save()
            bike_image = bike_image_form.save(commit=False)
            bike_image.bike = bike
            bike_image.save()
            return HttpResponseRedirect(reverse_lazy('home'))
        else:
            print(bike_image_form.errors)
            return render(request, self.template_name, context={"page": "create", "bike_form": bike_form, "bike_image_form": bike_image_form})


class DetailUpdateView(View):
    template_name = 'bike_app/create.html'
    fields = ('name', 'description', 'image')
    context_object_name = 'bike'

    def get(self, request, *args, **kwargs):
        bike = BikeModel.objects.get(id=self.kwargs['pk'])

        bike_form = BikeForm(
            instance=bike)
        return render(request, self.template_name, context={"page": "update", "bike_form": bike_form})

    def post(self, request, *args, **kwargs):
        bike = BikeModel.objects.get(id=self.kwargs['pk'])

        bike_form = BikeForm(request.POST, request.FILES, instance=bike)
        if bike_form.is_valid():
            bike = bike_form.save()
            return HttpResponseRedirect(reverse_lazy('details', kwargs={'pk': self.kwargs['pk']}))
        else:
            return render(request, self.template_name, context={"page": "create", "bike_form": bike_form})

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['page'] = 'update'
    #     context['']
    #     return context

    # def get_success_url(self):
    #     return reverse_lazy('details', kwargs={'pk': self.object.id})


# class BikeCreateView(CreateView, LoginRequiredMixin):
#     template_name = 'bike_app/create.html'
#     success_url = reverse_lazy('home')
#     model = BikeModel
#     fields = ('name', 'description', 'image')

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['page'] = 'create'
#         return context
