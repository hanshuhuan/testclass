# Generated by Django 4.2.11 on 2024-05-17 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_item_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
