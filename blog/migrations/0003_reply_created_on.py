# Generated by Django 3.0.7 on 2021-02-21 12:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_reply'),
    ]

    operations = [
        migrations.AddField(
            model_name='reply',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]