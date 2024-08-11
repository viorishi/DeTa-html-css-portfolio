from django.urls import path # forward urls from the main application
from .import views # set urls for view that belongs to a model

urlpatterns = [
    path("notes/", views.NoteListCreate.as_view(),name="note-list"),
    path("notes/delete/<int:pk>/", views.NoteDelete.as_view(), name="delete-note"),
] 


