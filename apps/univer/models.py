from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.db import models

class University(models.Model):
    title = models.CharField(
        _('Университет'), max_length=64, help_text=_('Введите название университета'), unique=True
    )
    description = models.TextField(
        _("Описание университета"), help_text=_("Введите описание университета")
    )


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Университеты')
        verbose_name_plural = _('Университеты')

class Professor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    univer = models.OneToOneField(University, on_delete=models.CASCADE)
    title = models.CharField(
        _('Название предмета преподования'), max_length=64, help_text=_('Введите название предмета который преподает учитель'), unique=True
    )
    bio = models.CharField(
        _('ФИО'), max_length=64, help_text=_('Введите полное имя'), unique=True
    )

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = _('Профессор')
        verbose_name_plural = _('Профессор')


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    univer = models.OneToOneField(University, on_delete=models.CASCADE)
    enrollment_date = models.DateTimeField(
        _("Дата начала учебы"),
        help_text=_("Дата и время начала учебы"),
    )
    graduation_date = models.DateTimeField(
        _("Дата окончания учебы"),
        help_text=_("Дата и время окончания учебы"),
    )

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = _('Студент')
        verbose_name_plural = _('Студент')

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    univer = models.OneToOneField(University, on_delete=models.CASCADE)
    CHOICES_METHOD = (
        ("professor", "professor"),
        ("student", "student"),

    )
    status = models.CharField(verbose_name='Учитель или студент?', max_length=16, choices=CHOICES_METHOD)
    bio = models.CharField(
        _('ФИО'), max_length=64, help_text=_('Введите полное имя'), unique=True
    )
    def __str__(self):
        return self.user

    class Meta:
        verbose_name = _('Профиль')
        verbose_name_plural = _('Профиль')

class Courses(models.Model):
    title = models.CharField(
        _('Название курса'), max_length=64, help_text=_('Введите название курса'), unique=True
    )
    description = models.TextField(
        _("Описание курса"), help_text=_("Введите описание курса")
    )

    code = models.IntegerField(
        _('код'),
        default=0,
        help_text=_('Введите промокод')
    )
    univer=models.ForeignKey(University,on_delete=models.CASCADE)
    professor=models.ForeignKey(Professor,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Курсы')
        verbose_name_plural = _('Курсы')

class Kabinet(models.Model):

    number = models.IntegerField(
        _('номер кабинета'),
        default=0,
        help_text=_('Введите номер кабинета')
    )
    building = models.IntegerField(
        _('этаж'),
        default=0,
        help_text=_('Введите номер этажа')
    )
    capacity = models.IntegerField(
        _('вместимость'),
        default=0,
        help_text=_('Введите вместимость аудитории')
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Кабинет')
        verbose_name_plural = _('Кабинет')

class Raspisanie(models.Model):
    courses=models.ForeignKey(Courses,on_delete=models.CASCADE)
    classes=models.ForeignKey(Kabinet,on_delete=models.CASCADE)
    start_time = models.CharField(_("Время начала курса"),max_length=16,
        help_text=_("Время начала курса"),
    )
    end_time = models.CharField(
        _("Время окончания курса"),max_length=16,
        help_text=_("Время окончания курса"),
    )

    CHOICES_METHOD = (
        ("Понедельник", "Понедельник"),
        ("Вторник", "Вторник"),
        ("Среда", "Среда"),
        ("Четверг", "Четверг"),
        ("Пятница", "Пятница"),
        ("Суббота", "Суббота"),
        ("Воскресенье", "Воскресенье"),

    )
    day_of_week = models.CharField(verbose_name='День недели', max_length=16, choices=CHOICES_METHOD)
    def __str__(self):
        return self.courses

    class Meta:
        verbose_name = _('Расписание')
        verbose_name_plural = _('Расписание')

class Zapic(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    course=models.ForeignKey(Courses,on_delete=models.CASCADE)
    date_enrolled = models.DateTimeField(
        _("Дата начала курса"),
        help_text=_("Дата и время начала курса"),
    )
    grade = models.IntegerField(
        _('Оценка'),
        default=0,
        help_text=_('Введите оценку')
    )
    def __str__(self):
        return self.student

    class Meta:
        verbose_name = _('Запись')
        verbose_name_plural = _('Запись')
class DZ(models.Model):
    course=models.ForeignKey(Courses,on_delete=models.CASCADE)
    title = models.CharField(
        _('Название домашнего задания'), max_length=64, help_text=_('Введите название дз'), unique=True
    )
    description = models.TextField(
        _("Описание дз"), help_text=_("Введите описание дз")
    )
    date_enrolled = models.DateTimeField(
        _("Дата окончания срока сдачи дз"),
        help_text=_("Дата окончания срока сдачи дз"),
    )
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('ДЗ')
        verbose_name_plural = _('ДЗ')


class Sdacha(models.Model):
    assignment=models.ForeignKey(DZ,on_delete=models.CASCADE)
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    submission_date = models.DateTimeField(
        _("Дата окончания срока сдачи дз"),
        help_text=_("Дата окончания срока сдачи дз"),
    )
    grade = models.IntegerField(
        _('Оценка'),
        default=0,
        help_text=_('Введите оценку')
    )
    feedback = models.TextField(
        _("Описание дз"), help_text=_("Введите описание дз")
    )

    def __str__(self):
        return self.feedback

    class Meta:
        verbose_name = _('Сдача')
        verbose_name_plural = _('Сдача')

