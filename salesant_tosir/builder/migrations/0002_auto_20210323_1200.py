# Generated by Django 3.1.7 on 2021-03-23 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('builder', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='build',
            name='id',
        ),
        migrations.AlterField(
            model_name='build',
            name='build_name',
            field=models.CharField(default='BuildName', max_length=200, primary_key=True, serialize=False),
        ),
    ]