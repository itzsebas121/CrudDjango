# Generated by Django 5.0.10 on 2024-12-19 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('productName', models.CharField(max_length=100)),
                ('supplierID', models.IntegerField()),
                ('categoryID', models.IntegerField()),
                ('quantityPerUnit', models.CharField(max_length=100)),
                ('unitPrice', models.IntegerField()),
                ('unitsInStock', models.IntegerField()),
                ('unitsOnOrder', models.IntegerField()),
                ('reorderLevel', models.IntegerField()),
                ('discontinued', models.BooleanField()),
            ],
        ),
    ]
