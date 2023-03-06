from django.core.validators import MaxValueValidator
from django.db import models
from clients.models import Client


class Service(models.Model):
    name = models.CharField('Имя', max_length=50)
    full_price = models.PositiveIntegerField('Цена')

    def __str__(self):
        return f'Сервис: {self.name} - {self.full_price}'


class Plan(models.Model):
    PLAN_TYPES = (
        ('full', 'Полный'),
        ('student', 'Студенческий'),
        ('discount', 'Скидочный'),
    )

    plan_type = models.CharField('Тип тарифа', choices=PLAN_TYPES, max_length=10)
    discount_percent = models.PositiveIntegerField('Скидка, %', default=0, validators=[MaxValueValidator(100), ])

    def __str__(self):
        return f'Тариф: {self.plan_type} {self.discount_percent}%'


class Subscription(models.Model):
    client = models.ForeignKey(Client, related_name='subscriptions', on_delete=models.PROTECT, verbose_name='Клиент')
    service = models.ForeignKey(Service, related_name='subscriptions', on_delete=models.PROTECT, verbose_name='Сервис')
    plan = models.ForeignKey(Plan, related_name='subscriptions', on_delete=models.PROTECT, verbose_name='Тариф')

    def __str__(self):
        return f'Подписка на {self.service} для {self.client} {self.plan}'
