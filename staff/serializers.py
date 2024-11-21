from rest_framework.serializers import ModelSerializer

from staff.models import Employee


class EmployeeSerializer(ModelSerializer):
    """Сериализатор для сотрудников."""
    class Meta:
        model = Employee
        fields = '__all__'