# Generated by Django 5.0.6 on 2024-06-25 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0004_alter_customer_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='work',
            old_name='Customer',
            new_name='customer',
        ),
    ]
