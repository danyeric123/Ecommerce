# Generated by Django 3.2.9 on 2021-11-10 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0003_auto_20211110_1724"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="category",
            field=models.ManyToManyField(to="products.Category"),
        ),
    ]
