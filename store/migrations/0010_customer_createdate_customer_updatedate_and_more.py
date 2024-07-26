# Generated by Django 5.0.6 on 2024-07-21 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_alter_product_discount_alter_product_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='createDate',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='updateDate',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='createDate',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='updateDate',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='createDate',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='updateDate',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]