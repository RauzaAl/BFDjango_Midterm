# Generated by Django 3.1.7 on 2021-03-20 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='role',
            field=models.PositiveIntegerField(choices=[(1, 'superadmin'), (2, 'guest')], null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.PositiveIntegerField(choices=[(1, 'male'), (2, 'female')], null=True),
        ),
    ]
