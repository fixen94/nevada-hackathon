from django.db import models

class TimeManager(models.Manager):
    def create_time(self, date):
        time = self.create(date=date)
        # do something with the book
        return time


class KassaManager(models.Manager):
    def create_kassa(self, kassa_no, persons, status, date):
        kassa = self.create(kassa_no=kassa_no, persons=persons, status=status, kassa_date=date)
        return kassa


class Alerts(models.Model):
    kassa = models.PositiveIntegerField("Касса №")
    date = models.DateTimeField("Время", auto_now_add=True)

    class Meta:
        ordering = ('-date',)
        verbose_name = "Полная касса"
        verbose_name_plural = "Полные кассы"

    def __str__(self):
        return self.kassa


class Time(models.Model):
    date = models.TextField("Дата и время")

    objects = TimeManager()

    class Meta:
        ordering = ('-date',)
        verbose_name = "время"
        verbose_name_plural = "время"

    def __str__(self):
        return self.date


class Kassa(models.Model):
    kassa_no = models.CharField("Касса №",max_length=10)
    status = models.CharField('Загружена?',max_length=20)
    persons = models.CharField('Количество человек', max_length=5)
    kassa_date = models.ForeignKey('Time', verbose_name='Время', related_name='kassa_no',
                                     on_delete=models.CASCADE)

    objects = KassaManager()

    class Meta:
        ordering = ('kassa_no',)
        verbose_name = "касса"
        verbose_name_plural = "кассы"

    def __str__(self):
        return self.kassa_no


