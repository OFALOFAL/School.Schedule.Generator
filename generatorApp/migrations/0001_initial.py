# Generated by Django 5.0 on 2024-02-23 20:05

import datetime
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
            name="ScheduleList",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                (
                    "created_date",
                    models.DateTimeField(
                        default=datetime.datetime(
                            2024, 2, 23, 20, 5, 0, 302925, tzinfo=datetime.timezone.utc
                        )
                    ),
                ),
                ("content", models.TextField()),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="LessonHours",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("start_hour", models.CharField(max_length=30)),
                ("duration", models.IntegerField()),
                (
                    "schedule_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="generatorApp.schedulelist",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ClassroomTypes",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("description", models.CharField(max_length=150)),
                (
                    "schedule_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="generatorApp.schedulelist",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Classrooms",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=30)),
                (
                    "type_id",
                    models.ForeignKey(
                        default=0,
                        on_delete=django.db.models.deletion.SET_DEFAULT,
                        to="generatorApp.classroomtypes",
                    ),
                ),
                (
                    "schedule_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="generatorApp.schedulelist",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SubjectNames",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                (
                    "schedule_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="generatorApp.schedulelist",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Teachers",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=30)),
                ("surname", models.CharField(max_length=30)),
                ("possible_subjects", models.CharField(max_length=300)),
                ("start_hour_index", models.CharField(max_length=30)),
                ("end_hour_index", models.CharField(max_length=30)),
                ("days", models.CharField(max_length=30)),
                (
                    "main_classroom_id",
                    models.ForeignKey(
                        default="Null",
                        on_delete=django.db.models.deletion.SET_DEFAULT,
                        to="generatorApp.classrooms",
                    ),
                ),
                (
                    "schedule_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="generatorApp.schedulelist",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Subject",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("subject_count_in_week", models.IntegerField()),
                ("number_of_groups", models.IntegerField()),
                ("max_stack", models.IntegerField()),
                ("classroom_types", models.CharField(max_length=30)),
                (
                    "classroom_id",
                    models.ForeignKey(
                        default="Null",
                        on_delete=django.db.models.deletion.SET_DEFAULT,
                        to="generatorApp.classrooms",
                    ),
                ),
                (
                    "lesson_hour_id",
                    models.ForeignKey(
                        default="Null",
                        on_delete=django.db.models.deletion.SET_DEFAULT,
                        to="generatorApp.lessonhours",
                    ),
                ),
                (
                    "schedule_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="generatorApp.schedulelist",
                    ),
                ),
                (
                    "subject_name_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="generatorApp.subjectnames",
                    ),
                ),
                (
                    "teacher_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="generatorApp.teachers",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Classes",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("grade", models.IntegerField()),
                ("class_signature", models.CharField(max_length=10)),
                (
                    "starting_lesson_hour_id",
                    models.ForeignKey(
                        default=0,
                        on_delete=django.db.models.deletion.SET_DEFAULT,
                        to="generatorApp.lessonhours",
                    ),
                ),
                (
                    "schedule_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="generatorApp.schedulelist",
                    ),
                ),
                (
                    "supervising_teacher_id",
                    models.ForeignKey(
                        default="Null",
                        on_delete=django.db.models.deletion.SET_DEFAULT,
                        to="generatorApp.teachers",
                    ),
                ),
            ],
        ),
    ]
