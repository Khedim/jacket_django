# Generated by Django 4.1.7 on 2023-03-01 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='place',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
