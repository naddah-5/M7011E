# Generated by Django 4.1.4 on 2022-12-31 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webstore', '0005_alter_product_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]