from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from movies.forms import FilmModelForm
from movies.models import *

def index(request):
    """Metoda připravuje pohled pro domovskou stránku - šablona index.html"""

    # Uložení celkového počtu filmů v databázi do proměnné num_films
    num_films = Film.objects.all().count()
    # Do proměnné films se uloží 3 filmy uspořádané podle hodnocení (sestupně)
    films = Film.objects.order_by('-rate')[:3]

    """ Do proměnné context, která je typu slovník (dictionary) uložíme hodnoty obou proměnných """
    context = {
        'num_films': num_films,
        'films': films
    }

    """ Pomocí metody render vyrendrujeme šablonu index.html a předáme ji hodnoty v proměnné context k zobrazení """
    return render(request, 'index.html', context=context)


class FilmListView(ListView):
    model = Film

    context_object_name = 'film_list'
    template_name = 'film/list.html'
    paginate_by = 2

    def get_queryset(self):
        if 'genre_name' in self.kwargs:
            return Film.objects.filter(genres__name=self.kwargs['genre_name']).all() # Get 5 books containing the title war
        else:
            return Film.objects.all()

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['num_films'] = len(self.get_queryset())
        if 'genre_name' in self.kwargs:
            context['view_title'] = f"Žánr: {self.kwargs['genre_name']}"
            context['view_head'] = f"Žánr filmu: {self.kwargs['genre_name']}"
        else:
            context['view_title'] = 'Filmy'
            context['view_head'] = 'Přehled filmů'
        return context


class FilmDetailView(DetailView):
    model = Film

    context_object_name = 'film_detail'
    template_name = 'film/detail.html'


def topten(request):
    return render(request, 'topten.html')


class FilmCreateView(CreateView):
    model = Film
    fields = ['title', 'plot', 'poster', 'genres', 'release_date', 'runtime', 'rate']


class FilmUpdateView(UpdateView):
    model = Film
    template_name = 'movies/film_bootstrap_form.html'
    form_class = FilmModelForm


class FilmDeleteView(DeleteView):
    model = Film
    success_url = reverse_lazy('film_list')