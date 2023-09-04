import datetime
import json

from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from typing import Literal, Union

from .models import Task, TaskAssigned
from .serializers import TaskAssignedSerializer
from users.models import User, UserRole


STATUS = {'PROCESO':'proceso', 'FINALIZADO': 'finalizado'}


@login_required
@api_view(['GET'])
def get_my_tasks(request: Request) -> list[dict]:
    user_pk = request.user.pk
    query_set_tasks = TaskAssigned.objects.filter(user_who_owns_id=user_pk)
    tasks = TaskAssignedSerializer(query_set_tasks, many=True)

    return Response(tasks.data)


@login_required
@api_view(['POST'])
def create_task(request: Request, user_pk: str, task_id: str) -> dict[str, str]:
    admin_pk = request.user.pk
    admin_role = get_object_or_404(UserRole, user_id=admin_pk).role
    if admin_role == 'admin':
        current_week = datetime.date.today().isocalendar()[1]
        tasks_by_week = TaskAssigned.objects.filter(
            user_who_owns_id=user_pk, week=current_week)

        if tasks_by_week.count() < 3:
            task_assigned_to_user = TaskAssigned(
                creator_user=get_object_or_404(User, pk=admin_pk),
                user_who_owns=get_object_or_404(User, pk=user_pk),
                task=get_object_or_404(Task, pk=task_id),
                week=current_week,
                status=STATUS['PROCESO']
            )
            task_assigned_to_user.save()

            return Response({"message": "Tarea creada con éxito"})

        return Response({"message": "El usuario ya cuenta con 3 tareas asignadas para esta semana"})

    return Response({"message": "El usuario no es administrador"})


@login_required
@api_view(['PATCH'])
def finish_task(request: Request, task_id: str) -> dict[str, str]:
    user_pk = request.user.pk
    current_week = datetime.date.today().isocalendar()[1]
    task = get_object_or_404(TaskAssigned, user_who_owns_id=user_pk, task_id=task_id, week=current_week)
    task.status = STATUS['FINALIZADO']
    task.save()

    return Response({"message": "La tarea fue finalizada"})
