# Generated by Django 5.0.3 on 2024-03-23 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_issue_return_return_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='history',
            fields=[
                ('student_id', models.IntegerField(primary_key=True, serialize=False)),
                ('student_name', models.CharField(max_length=50)),
                ('phone', models.IntegerField()),
                ('class_dept', models.CharField(max_length=100)),
                ('roll_no', models.IntegerField()),
                ('year', models.DateField()),
            ],
        ),
    ]
