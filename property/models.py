from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Flat(models.Model):
    created_at = models.DateTimeField(
        'Когда создано объявление',
        default=timezone.now,
        db_index=True)

    description = models.TextField('Текст объявления', blank=True)
    price = models.IntegerField('Цена квартиры', db_index=True)

    town = models.CharField(
        'Город, где находится квартира',
        max_length=50,
        db_index=True)
    town_district = models.CharField(
        'Район города, где находится квартира',
        max_length=50,
        blank=True,
        help_text='Чертаново Южное')
    address = models.TextField(
        'Адрес квартиры',
        help_text='ул. Подольских курсантов д.5 кв.4')
    floor = models.CharField(
        'Этаж',
        max_length=3,
        help_text='Первый этаж, последний этаж, пятый этаж')

    number_of_rooms = models.IntegerField(
        'Количество комнат в квартире',
        db_index=True)
    living_area = models.IntegerField(
        'количество жилых кв.метров',
        null=True,
        blank=True,
        db_index=True)

    has_balcony = models.NullBooleanField('Наличие балкона', db_index=True)
    is_active = models.BooleanField('Активно-ли объявление', db_index=True)
    is_new_building = models.NullBooleanField('Новостройка', db_index=True)
    construction_year = models.IntegerField(
        'Год постройки здания',
        null=True,
        blank=True,
        db_index=True)
    likes = models.ManyToManyField(User, related_name='liked_flats',
                                   blank=True, verbose_name='Кто лайкнул:')

    def __str__(self):
        return f'{self.town}, {self.address} ({self.price}р.)'

    class Meta:
        verbose_name = 'Квартира'
        verbose_name_plural = 'Квартиры'


class Complaint(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               verbose_name='Кто жаловался:',
                               related_name='complaints')
    flat = models.ForeignKey(Flat, on_delete=models.CASCADE,
                             verbose_name='Квартира, на которую жаловались:',
                             related_name='complaints')
    text = models.TextField('Текст жалобы:')

    class Meta:
        verbose_name = 'Жалобы'
        verbose_name_plural = 'Жалобы'


class Owner(models.Model):
    fio = models.CharField('ФИО владельца:', max_length=200, db_index=True)
    phone_number = models.CharField('Номер владельца:', max_length=20)
    pure_phone_number = PhoneNumberField('Нормализованный номер владельца',
                                         blank=True, db_index=True)
    flats = models.ManyToManyField(Flat, related_name='owners', blank=True,
                                   verbose_name='Квартиры в собственности')

    def __str__(self):
        return self.fio

    class Meta:
        verbose_name = 'Собственник'
        verbose_name_plural = 'Собственники'
