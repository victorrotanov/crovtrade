# Generated by Django 5.1.7 on 2025-03-10 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_product_alter_news_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='start_price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
