# Generated by Django 5.1.4 on 2025-04-08 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='discount',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='تخفیف روی فاکتور'),
        ),
    ]
