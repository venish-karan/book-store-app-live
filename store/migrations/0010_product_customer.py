# Generated by Django 3.2.6 on 2021-12-21 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_alter_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='customer',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.customer'),
        ),
    ]