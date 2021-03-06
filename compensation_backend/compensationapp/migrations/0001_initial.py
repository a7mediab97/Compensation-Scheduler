# Generated by Django 3.0.1 on 2019-12-20 13:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='CalendarHoliday',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('holiday_name', models.CharField(max_length=200)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='LectureGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lecture_group_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('room_type', models.CharField(choices=[('Room', 'Room'), ('Lab', 'Lab'), ('Small Hall', 'Small Hall'), ('Large Hall', 'Large Hall')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='WeekDay',
            fields=[
                ('day', models.PositiveIntegerField(choices=[(1, 'Saturday'), (2, 'Sunday'), (3, 'Monday'), (4, 'Tuesday'), (5, 'Wednesday'), (6, 'Thursday')], primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='TutorialGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tutorial_group_name', models.CharField(max_length=200)),
                ('holidays', models.ManyToManyField(to='compensationapp.WeekDay')),
                ('lecture_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compensationapp.LectureGroup')),
            ],
        ),
        migrations.CreateModel(
            name='StaffMember',
            fields=[
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('holidays', models.ManyToManyField(to='compensationapp.WeekDay')),
            ],
        ),
        migrations.CreateModel(
            name='Preferences',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_preffered', models.BooleanField()),
                ('slot', models.PositiveIntegerField(choices=[(1, '1ST'), (2, '2ND'), (3, '3RD'), (4, '4TH'), (5, '5TH')])),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compensationapp.WeekDay')),
                ('staff_member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compensationapp.StaffMember')),
            ],
        ),
        migrations.CreateModel(
            name='CourseMeeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot', models.PositiveIntegerField(choices=[(1, '1ST'), (2, '2ND'), (3, '3RD'), (4, '4TH'), (5, '5TH')])),
                ('slot_type', models.PositiveIntegerField(choices=[(1, 'Tutorial'), (2, 'Lab'), (3, 'Lecture')])),
                ('course_start_date', models.DateField()),
                ('course_end_date', models.DateField()),
                ('midterm_start_date', models.DateField()),
                ('midterm_end_date', models.DateField()),
                ('is_first_year', models.BooleanField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compensationapp.Course')),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compensationapp.WeekDay')),
                ('lecture_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compensationapp.LectureGroup')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compensationapp.Room')),
                ('staff_member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compensationapp.StaffMember')),
                ('tutorial_group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='compensationapp.TutorialGroup')),
            ],
        ),
        migrations.CreateModel(
            name='Compensation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('slot', models.PositiveIntegerField(choices=[(1, '1ST'), (2, '2ND'), (3, '3RD'), (4, '4TH'), (5, '5TH')])),
                ('course_meeting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compensationapp.CourseMeeting')),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compensationapp.WeekDay')),
                ('holiday', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compensationapp.CalendarHoliday')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compensationapp.Room')),
            ],
        ),
        migrations.AddField(
            model_name='calendarholiday',
            name='day',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compensationapp.WeekDay'),
        ),
    ]
