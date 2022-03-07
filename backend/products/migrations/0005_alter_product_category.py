# Generated by Django 3.2.9 on 2021-11-11 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0004_alter_product_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="category",
            field=models.ManyToManyField(
                to="products.Category", verbose_name="categories"
            ),
        ),
    ]
