# Generated by Django 4.0.3 on 2022-04-07 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0005_rename_id_fooditems_ide'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderood',
            name='custmizations',
        ),
        migrations.AlterField(
            model_name='orderood',
            name='foodid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basic.fooditems'),
        ),
    ]