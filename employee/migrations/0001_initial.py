# Generated by Django 3.1.5 on 2023-09-21 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('App_name', models.CharField(max_length=16)),
                ('App_intro', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Dep_name', models.CharField(max_length=16)),
                ('Dep_intro', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Role_name', models.CharField(max_length=16)),
                ('Role_intro', models.CharField(max_length=256)),
            ],
        ),
    ]