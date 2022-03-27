from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

# class Language(models.Model):
#     name = models.CharField(max_length=255)
#
#     def __str__(self):
#         return f"{self.name}"

class Diagnosis(models.Model):
    name = models.CharField(max_length=1024)
    class Meta:
        verbose_name = ""
        verbose_name_plural = ""
    def __str__(self):
        return f"{self.name}"

class Treatment(models.Model):
    name = models.CharField(max_length=1024)
    def __str__(self):
        return f"{self.name}"


class DentalFilling(models.Model):
    name = models.CharField(max_length=1024)
    def __str__(self):
        return f"{self.name}"



class BotUser(models.Model):
    # username = models.CharField(max_length=255, blank=True, null=True)
    # first_name = models.CharField(max_length=255, blank=True, null=True)
    full_name = models.CharField(verbose_name='ФИО',max_length=255, blank=True, null=True)
    # user_telegram_id = models.IntegerField(default=0)
    # language = models.ForeignKey(Language, on_delete=models.SET_NULL, blank=True, null=True)
    # register_status = models.BooleanField(default=False)
    phone = models.CharField("Телефон",max_length=255, blank=True, null=True)
    create_time = models.DateTimeField("Создать время", auto_now_add=True)
    update_time = models.DateTimeField("Время обновления",auto_now=True)
    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural='Клиенты'
    def __str__(self):
        return f"{self.full_name} -- {self.phone}"

class Procedure(models.Model):

    user = models.ForeignKey(BotUser, on_delete=models.SET_NULL, blank=True, null=True)
    diagnosis = models.ManyToManyField(Diagnosis)
    treatment = models.ManyToManyField(Treatment)
    dental_filling = models.ManyToManyField(DentalFilling)
    description = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name_plural = 'Процедуры'
        verbose_name = 'Процедура'
    def __str__(self):
        return f"{self.user} -- {self.create_time}"