from django.urls import path

from . import views

urlpatterns = [
    path("", views.get_my_tasks, name="get_my_tasks"),
    path("create-task/<int:user_pk>/<int:task_id>/", views.create_task, name="create_task"),
    path("finish-task/<int:task_id>/", views.finish_task, name="finish_task"),
]