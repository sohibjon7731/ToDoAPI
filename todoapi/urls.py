from django.urls import path

from todoapi.views import taskList, taskAdd, taskDetail, taskUpdate, taskDelete

urlpatterns=[
    path('task_list/', taskList, name='task-list'),
    path('task_add/',taskAdd, name='task-add'),
    path('task_detail/<int:pk>/', taskDetail, name='task-detail'),
    path('task_update/<int:pk>/', taskUpdate, name='task-update'),
    path('task_delete/<int:pk>', taskDelete, name='task-delete'),
]