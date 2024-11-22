from django.urls import path

from staff.apps import StaffConfig
from staff.views import EmployeeListAPIView, EmployeeCreateAPIView, EmployeeUpdateAPIView, EmployeeDestroyAPIView, \
    EmployeeRetrieveAPIView, TaskListAPIView, TaskCreateAPIView, TaskUpdateAPIView, TaskDestroyAPIView, \
    TaskRetrieveAPIView, EmployeeWithTaskListAPIView

app_name = StaffConfig.name

urlpatterns = [
    # Урлы для сотрудников
    path('employee_list/', EmployeeListAPIView.as_view(), name='employee-list'),
    path('employee_create/', EmployeeCreateAPIView.as_view(), name='employee-create'),
    path('<int:pk>/employee_update/', EmployeeUpdateAPIView.as_view(), name='employee-update'),
    path('<int:pk>/employee_destroy/', EmployeeDestroyAPIView.as_view(), name='employee-destroy'),
    path('<int:pk>/employee_retrieve/', EmployeeRetrieveAPIView.as_view(), name='employee-retrieve'),

    # Урлы для задач
    path('task_list/', TaskListAPIView.as_view(), name='task-list'),
    path('task_create/', TaskCreateAPIView.as_view(), name='task-create'),
    path('<int:pk>/task_update/', TaskUpdateAPIView.as_view(), name='task-update'),
    path('<int:pk>/task_destroy/', TaskDestroyAPIView.as_view(), name='task-destroy'),
    path('<int:pk>/task_retrieve/', TaskRetrieveAPIView.as_view(), name='task-retrieve'),

    # Урл для получения списка сотрудников вместе с их задачами
    path('employee_with_task_list/', EmployeeWithTaskListAPIView.as_view(), name='employee_with_task-list'),
]
