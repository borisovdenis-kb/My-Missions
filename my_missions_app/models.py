from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _


class CustomUser(AbstractUser):
    """
        Расширение стандартного юзера
        Добавляем:
        --- Номер телефона
        --- Аватар
    """

    avatar = models.ImageField(upload_to='avatar/', blank=True, max_length=1000)
    # телефон хранится в формате +7*********
    phone = models.CharField(max_length=12, blank=True)
    # сохраняем последние открытые задачи
    last_cat = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return '%s, %s, %s' % (
            self.username,
            self.phone,
            self.last_cat,
        )


class Category(models.Model):
    """ Таблица категорий """
    cat_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=80, blank=True, null=True)
    description = models.CharField(max_length=256, blank=True, null=True)
    user_id = models.ForeignKey(CustomUser, models.DO_NOTHING)

    def __str__(self):
        return '%s->%s' % (
            self.user_id,
            self.title,
        )

    class Meta:
        managed = True
        db_table = 'catalogs'


class Missions(models.Model):
    """ Таблица задач, котрые нужно выполнить юзеру"""
    mission_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    cat_id = models.ForeignKey(Category, models.DO_NOTHING)
    until_datetime = models.DateTimeField()
    remind_datetime = models.DateTimeField()

    def __str__(self):
        return '%s->%s->%s' % (
            self.cat_id.user_id.username,
            self.cat_id.title,
            self.name
        )

    class Meta:
        managed = True
        db_table = 'missions'


class RemindLoop(models.Model):
    mission = models.ForeignKey(Missions, models.DO_NOTHING)
    day = models.ForeignKey('WeekDays', models.DO_NOTHING)

    def __str__(self):
        return '%s->%s->%s | %s' % (
            self.mission.cat_id.user_id.username,
            self.mission.cat_id.title,
            self.mission.name,
            self.day.name
        )

    class Meta:
        managed = True
        db_table = 'remind_loop'
        unique_together = (('mission', 'day'),)


class WeekDays(models.Model):
    day_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return '%s' % (
            self.name
        )

    class Meta:
        managed = True
        db_table = 'week_days'