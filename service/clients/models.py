from django.contrib.auth.models import User
from django.db import models


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, verbose_name='Пользователь')
    company_name = models.CharField('Организация', max_length=100)
    full_address = models.CharField('Адрес', max_length=100)

    def __str__(self):
        return f'Клиент: {self.company_name}'