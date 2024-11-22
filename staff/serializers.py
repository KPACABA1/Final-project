from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from staff.models import Employee, Task


class EmployeeSerializer(ModelSerializer):
    """Сериализатор для сотрудников."""
    class Meta:
        model = Employee
        fields = '__all__'


class TaskSerializer(ModelSerializer):
    """Сериализатор для задач, кроме создания."""
    def validate_status(self, value):
        """Проверка, если задачу отредактировали и поставили в статус True, удаляю задачу и вычёркиваю её из общего
        числа задач сотрудника."""
        if value:
            employee = Employee.objects.get(full_name=self.instance.employee)
            employee.task_count -= 1
            employee.save()
            self.instance.delete()
            raise serializers.ValidationError("Экземпляр модели был удалён, потому что задача выполнена.")
        return value

    class Meta:
        model = Task
        fields = '__all__'


class TaskCreateSerializer(ModelSerializer):
    """Сериализатор для создания задач."""
    def validate_status(self, value):
        """Проверка на то, что статус у задачи - False."""
        if value:
            raise serializers.ValidationError("Поле 'status' не может быть True при создании задачи.")
        return value

    def validate_employee(self, value):
        """Проверка на то, назначили ли задаче при создании сотрудника или нет."""
        if value:
            employee = Employee.objects.get(full_name=value)
            employee.task_count += 1
            employee.save()
        return value

    class Meta:
        model = Task
        fields = '__all__'


class EmployeeWithTaskSerializer(ModelSerializer):
    """Сериализатор для сотрудников, который дополнительно выводит список их задач."""
    task= SerializerMethodField()

    def get_task(self, employee):
        """Метод для получения задач сотрудника."""
        return [task.pk for task in Task.objects.filter(employee=employee.pk)]

    class Meta:
        model = Employee
        fields = '__all__'
