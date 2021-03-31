# Generated by Django 3.1.7 on 2021-03-24 13:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('triggers', '0004_usertriggers_website'),
    ]

    operations = [
        migrations.RenameField(
            model_name='triggers',
            old_name='file',
            new_name='css_file',
        ),
        migrations.AddField(
            model_name='triggers',
            name='js_file',
            field=models.FileField(default=django.utils.timezone.now, upload_to='triggers/'),
            preserve_default=False,
        ),
    ]