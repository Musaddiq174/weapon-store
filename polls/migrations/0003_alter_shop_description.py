# Generated by Django 5.1 on 2024-09-09 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_shop_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='description',
            field=models.TextField(null=True),
        ),
    ]