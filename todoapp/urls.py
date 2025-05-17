from django.urls import path
from .views import task_list, task_create, task_append, task_delete, task_completed

urlpatterns = [
    path('', task_list, name="task_list"),
    path('task/create', task_create, name="create-task"),
    path('task/append/<int:pk>/', task_append, name="task_append"),
    path('task/delete/<int:pk>/', task_delete, name="task_delete"),
    path('task/completed/<int:pk>/', task_completed, name="task_completed"),

]