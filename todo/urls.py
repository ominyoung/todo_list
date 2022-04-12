from django.urls import path

from . import views

app_name = 'todo'
urlpatterns = [
    path('todo/', views.TodoVueOnlyTV.as_view(), name='vonly'),
]
