# Generated by Django 4.1.3 on 2022-11-25 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=255)),
                ('image', models.ImageField(blank=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Passwords',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('hash', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=16)),
                ('stock', models.IntegerField()),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('create_time', models.DateTimeField()),
                ('role', models.CharField(choices=[('CM', 'Customer'), ('AD', 'Admin'), ('SU', 'Superuser')], default='CM', max_length=2)),
                ('password', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webstore.passwords')),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('text', models.TextField(blank=True)),
                ('create_time', models.DateTimeField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webstore.products')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webstore.users')),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('order_date', models.DateTimeField()),
                ('address', models.TextField()),
                ('status', models.CharField(choices=[('PS', 'Processing'), ('PG', 'Packaging'), ('SH', 'Shipping'), ('PU', 'Pickup'), ('DV', 'Delivered')], default='PS', max_length=2)),
                ('delivery', models.DateTimeField(blank=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webstore.users')),
            ],
        ),
        migrations.CreateModel(
            name='OrderProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('price', models.DecimalField(decimal_places=2, max_digits=16)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webstore.orders')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webstore.products')),
            ],
            options={
                'unique_together': {('product_id', 'order_id')},
            },
        ),
        migrations.CreateModel(
            name='CartProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webstore.products')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webstore.users')),
            ],
            options={
                'unique_together': {('user_id', 'product_id')},
            },
        ),
    ]
