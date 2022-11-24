# Generated by Django 4.1.3 on 2022-11-24 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webstore', '0002_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='Role',
            field=models.CharField(choices=[('CM', 'Customer'), ('AD', 'Admin'), ('SU', 'Superuser')], default='CM', max_length=2),
        ),
    ]