# Generated by Django 4.1.3 on 2022-12-29 01:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateTimeField()),
                ('address', models.TextField()),
                ('status', models.CharField(choices=[('PS', 'Processing'), ('PG', 'Packaging'), ('SH', 'Shipping'), ('PU', 'Pickup'), ('DV', 'Delivered')], default='PS', max_length=2)),
                ('delivery', models.DateTimeField(blank=True, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=16)),
                ('stock', models.IntegerField(default=0)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('CM', 'Customer'), ('AD', 'Admin'), ('SU', 'Superuser')], default='CM', max_length=2)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'UserProfiles',
                'db_table': 'user_profile',
            },
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=255)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webstore.category')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('text', models.TextField(blank=True)),
                ('create_time', models.DateTimeField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webstore.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('price', models.DecimalField(decimal_places=2, max_digits=16)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='webstore.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='webstore.product')),
            ],
            options={
                'unique_together': {('product_id', 'order_id')},
            },
        ),
        migrations.CreateModel(
            name='InSubcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webstore.product')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webstore.subcategory')),
            ],
            options={
                'unique_together': {('product', 'subcategory')},
            },
        ),
        migrations.CreateModel(
            name='InCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webstore.category')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webstore.product')),
            ],
            options={
                'unique_together': {('product', 'category')},
            },
        ),
        migrations.CreateModel(
            name='CartProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webstore.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user_id', 'product_id')},
            },
        ),
    ]
