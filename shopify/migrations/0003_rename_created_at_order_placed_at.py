# Generated by Django 5.1.4 on 2025-01-01 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopify', '0002_alter_product_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='created_at',
            new_name='placed_at',
        ),
    ]