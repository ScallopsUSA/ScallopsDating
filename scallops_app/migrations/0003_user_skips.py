# Generated by Django 3.1 on 2020-09-16 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scallops_app', '0002_auto_20200708_1204'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='skips',
            field=models.ManyToManyField(related_name='_user_skips_+', to='scallops_app.User'),
        ),
    ]