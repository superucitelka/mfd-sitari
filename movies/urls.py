from django.urls import path

from movies import views

urlpatterns = [
    path('', views.index, name='index'),
    path('films/', views.FilmListView.as_view(), name='film_list'),
    path('films/<int:pk>/', views.FilmDetailView.as_view(), name='film-detail'),
    path('films/genres/<str:genre_name>/', views.FilmListView.as_view(), name='film_genre'),
    path('topten', views.topten, name='topten'),
    path('film/create/', views.FilmCreateView.as_view(), name='film-create'),
    path('film/<int:pk>/update/', views.FilmUpdateView.as_view(), name='film-update'),
    path('film/<int:pk>/delete/', views.FilmDeleteView.as_view(), name='film-delete'),
]
