# Generated by Django 3.0.1 on 2019-12-21 22:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('compensationapp', '0002_lecturegroup_semester'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursemeeting',
            name='tutorial_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='compensationapp.TutorialGroup'),
        ),
    ]
