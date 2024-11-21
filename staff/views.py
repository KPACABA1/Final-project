from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView

from staff.models import Employee
from staff.serializers import EmployeeSerializer


class EmployeeListAPIView(ListAPIView):
    """Класс для вывода всех сотрудников."""
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeRetrieveAPIView(RetrieveAPIView):
    """Класс для просмотра детальной информации о сотруднике"""
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeCreateAPIView(CreateAPIView):
    """Класс для создания сотрудника."""
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer



class EmployeeUpdateAPIView(UpdateAPIView):
    """Класс для редактирования сотрудников."""
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeDestroyAPIView(DestroyAPIView):
    """Класс для удаления сотрудников."""
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
