# Generated by Django 3.1.1 on 2020-09-06 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20200906_0626'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productpost',
            old_name='category',
            new_name='cat',
        ),
    ]
