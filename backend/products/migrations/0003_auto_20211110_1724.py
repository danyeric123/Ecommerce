# Generated by Django 3.2.9 on 2021-11-10 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0002_auto_20211110_1637"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="category",
        ),
        migrations.AddField(
            model_name="product",
            name="category",
            field=models.ManyToManyField(null=True, to="products.Category"),
        ),
    ]
