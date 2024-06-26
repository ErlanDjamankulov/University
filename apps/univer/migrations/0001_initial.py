# Generated by Django 5.0.6 on 2024-06-08 15:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Введите название курса', max_length=64, unique=True, verbose_name='Название курса')),
                ('description', models.TextField(help_text='Введите описание курса', verbose_name='Описание курса')),
                ('code', models.IntegerField(default=0, help_text='Введите промокод', verbose_name='код')),
            ],
            options={
                'verbose_name': 'Курсы',
                'verbose_name_plural': 'Курсы',
            },
        ),
        migrations.CreateModel(
            name='Kabinet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=0, help_text='Введите номер кабинета', verbose_name='номер кабинета')),
                ('building', models.IntegerField(default=0, help_text='Введите номер этажа', verbose_name='этаж')),
                ('capacity', models.IntegerField(default=0, help_text='Введите вместимость аудитории', verbose_name='вместимость')),
            ],
            options={
                'verbose_name': 'Кабинет',
                'verbose_name_plural': 'Кабинет',
            },
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Введите название университета', max_length=64, unique=True, verbose_name='Университет')),
                ('description', models.TextField(help_text='Введите описание университета', verbose_name='Описание университета')),
            ],
            options={
                'verbose_name': 'Университеты',
                'verbose_name_plural': 'Университеты',
            },
        ),
        migrations.CreateModel(
            name='DZ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Введите название дз', max_length=64, unique=True, verbose_name='Название домашнего задания')),
                ('description', models.TextField(help_text='Введите описание дз', verbose_name='Описание дз')),
                ('date_enrolled', models.DateTimeField(help_text='Дата окончания срока сдачи дз', verbose_name='Дата окончания срока сдачи дз')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='univer.courses')),
            ],
            options={
                'verbose_name': 'ДЗ',
                'verbose_name_plural': 'ДЗ',
            },
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Введите название предмета который преподает учитель', max_length=64, unique=True, verbose_name='Название предмета преподования')),
                ('bio', models.CharField(help_text='Введите полное имя', max_length=64, unique=True, verbose_name='ФИО')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('univer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='univer.university')),
            ],
            options={
                'verbose_name': 'Профессор',
                'verbose_name_plural': 'Профессор',
            },
        ),
        migrations.AddField(
            model_name='courses',
            name='professor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='univer.professor'),
        ),
        migrations.CreateModel(
            name='Raspisanie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.CharField(help_text='Время начала курса', max_length=16, verbose_name='Время начала курса')),
                ('end_time', models.CharField(help_text='Время окончания курса', max_length=16, verbose_name='Время окончания курса')),
                ('day_of_week', models.CharField(choices=[('Понедельник', 'Понедельник'), ('Вторник', 'Вторник'), ('Среда', 'Среда'), ('Четверг', 'Четверг'), ('Пятница', 'Пятница'), ('Суббота', 'Суббота'), ('Воскресенье', 'Воскресенье')], max_length=16, verbose_name='День недели')),
                ('classes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='univer.kabinet')),
                ('courses', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='univer.courses')),
            ],
            options={
                'verbose_name': 'Расписание',
                'verbose_name_plural': 'Расписание',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enrollment_date', models.DateTimeField(help_text='Дата и время начала учебы', verbose_name='Дата начала учебы')),
                ('graduation_date', models.DateTimeField(help_text='Дата и время окончания учебы', verbose_name='Дата окончания учебы')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('univer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='univer.university')),
            ],
            options={
                'verbose_name': 'Студент',
                'verbose_name_plural': 'Студент',
            },
        ),
        migrations.CreateModel(
            name='Sdacha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submission_date', models.DateTimeField(help_text='Дата окончания срока сдачи дз', verbose_name='Дата окончания срока сдачи дз')),
                ('grade', models.IntegerField(default=0, help_text='Введите оценку', verbose_name='Оценка')),
                ('feedback', models.TextField(help_text='Введите описание дз', verbose_name='Описание дз')),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='univer.dz')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='univer.student')),
            ],
            options={
                'verbose_name': 'Сдача',
                'verbose_name_plural': 'Сдача',
            },
        ),
        migrations.AddField(
            model_name='courses',
            name='univer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='univer.university'),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('professor', 'professor'), ('student', 'student')], max_length=16, verbose_name='Учитель или студент?')),
                ('bio', models.CharField(help_text='Введите полное имя', max_length=64, unique=True, verbose_name='ФИО')),
                ('univer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='univer.university')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профиль',
            },
        ),
        migrations.CreateModel(
            name='Zapic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_enrolled', models.DateTimeField(help_text='Дата и время начала курса', verbose_name='Дата начала курса')),
                ('grade', models.IntegerField(default=0, help_text='Введите оценку', verbose_name='Оценка')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='univer.courses')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='univer.student')),
            ],
            options={
                'verbose_name': 'Запись',
                'verbose_name_plural': 'Запись',
            },
        ),
    ]
