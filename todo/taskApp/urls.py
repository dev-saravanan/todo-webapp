from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('complete/<id>', views.completed),
    path('not_complete/<id>', views.notCompleted),
    path('delete_task/<id>', views.deleteTask),
    path('update_task/<id>', views.updateTask),
]
