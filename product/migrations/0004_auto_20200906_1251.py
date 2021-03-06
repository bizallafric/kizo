# Generated by Django 3.1.1 on 2020-09-06 19:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20200906_0705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productpost',
            name='cat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_cat', to='product.category'),
        ),
        migrations.AlterField(
            model_name='productpost',
            name='subcat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_subcategory', to='product.subcategory'),
        ),
    ]
