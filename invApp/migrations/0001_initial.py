# Generated by Django 3.1.7 on 2021-02-25 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_sku', models.CharField(max_length=10)),
                ('nama_produk', models.CharField(max_length=100)),
            ],
        ),
    ]
