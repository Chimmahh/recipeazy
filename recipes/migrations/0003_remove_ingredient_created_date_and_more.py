# Generated by Django 5.0 on 2023-12-21 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_alter_ingredient_created_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='ingredient',
            name='last_update',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='last_update',
        ),
        migrations.AddField(
            model_name='ingredient',
            name='created',
            field=models.DateTimeField(editable=False, null=True),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='modified',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='created',
            field=models.DateTimeField(editable=False, null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='modified',
            field=models.DateTimeField(null=True),
        ),
    ]
