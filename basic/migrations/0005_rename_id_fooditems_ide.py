# Generated by Django 4.0.3 on 2022-03-31 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0004_alter_customer_uname_alter_fooditems_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fooditems',
            old_name='id',
            new_name='ide',
        ),
    ]