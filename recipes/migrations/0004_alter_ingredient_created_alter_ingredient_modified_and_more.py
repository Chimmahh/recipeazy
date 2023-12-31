# Generated by Django 5.0 on 2023-12-21 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_remove_ingredient_created_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='created',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='modified',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='created',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='modified',
            field=models.DateField(auto_now=True),
        ),
    ]
