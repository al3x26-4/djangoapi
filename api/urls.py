from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('stories/', views.getStories, name="stories"),
    path('notes/', views.getNotes, name="notes"),
    path('notes/create/', views.createNote, name="create-note"),
    path('notes/<str:pk>/update/', views.updateNote, name="update-note"),
    path('notes/<str:pk>/delete/', views.deleteNote, name="delete-note"),
    path('<slug:category_slug>/', views.category, name='category'),

    path('notes/<str:pk>/', views.getNote, name="note"),
    path('stories/<str:pk>/', views.getStory, name="story"),
]
