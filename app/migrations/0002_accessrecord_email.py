# Generated by Django 4.2 on 2023-08-22 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='accessrecord',
            name='email',
            field=models.EmailField(default='shashi@gmail.com', max_length=254),
        ),
    ]
