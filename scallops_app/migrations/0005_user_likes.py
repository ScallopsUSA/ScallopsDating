# Generated by Django 3.0.7 on 2020-06-25 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scallops_app', '0004_auto_20200625_1255'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='likes',
            field=models.ManyToManyField(related_name='_user_likes_+', to='scallops_app.User'),
        ),
    ]
