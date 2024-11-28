from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from staff.models import Employee


class EmployeeTestCase(APITestCase):
    """Тесты для CRUD сотрудников."""
    def setUp(self):
        """Создаю пользователя для тестов"""
        self.employee = Employee.objects.create(full_name='test_1', post='test_1')

    def test_employee_create(self):
        """Тест на создание пользователя."""
        # Arrange(подготавливаю данные для теста)
        url = reverse('staff:employee-create')

        # Act(совершаю действие которое тестирую)
        data = {'full_name': 'test_2', 'post': 'test_2'}
        response = self.client.post(url, data)

        # Assert(делаю проверки)
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )
        self.assertEqual(
            Employee.objects.all().count(), 2
        )

    def test_employee_update(self):
        """Тест на обновление пользователя."""
        # Arrange(подготавливаю данные для теста)
        url = reverse('staff:employee-update', args=(self.employee.pk,))

        # Act(совершаю действие которое тестирую)
        data = {'full_name': 'test_new'}
        response = self.client.patch(url, data)
        data = response.json()

        # Assert(делаю проверки)
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('full_name'), 'test_new'
        )

    def test_employee_delete(self):
        """Тест на удаление пользователя."""
        # Arrange(подготавливаю данные для теста)
        url = reverse('staff:employee-destroy', args=(self.employee.pk,))

        # Act(совершаю действие которое тестирую)
        response = self.client.delete(url)

        # Assert(делаю проверки)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Employee.objects.all().count(), 0
        )

    def test_employee_retrieve(self):
        """Тест на детальный просмотр пользователя."""
        # Arrange(подготавливаю данные для теста)
        url = reverse('staff:employee-retrieve', args=(self.employee.pk,))

        # Act(совершаю действие которое тестирую)
        response = self.client.get(url)
        data = response.json()

        # Assert(делаю проверки)
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('full_name'), self.employee.full_name
        )

    def test_employee_list(self):
        """Тест на просмотр всех пользователей."""
        # Arrange(подготавливаю данные для теста)
        url = reverse('staff:employee-list')

        # Act(совершаю действие которое тестирую)
        response = self.client.get(url)

        # Assert(делаю проверки)
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        result = [
            {
                "id": self.employee.pk,
                "full_name": self.employee.full_name,
                "post": self.employee.post,
                "task_count": self.employee.task_count
            }
        ]
        data = response.json()
        self.assertEqual(
            data, result
        )
