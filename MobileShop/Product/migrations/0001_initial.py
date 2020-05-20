# Generated by Django 2.2 on 2020-04-16 07:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=150, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=120, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color_name', models.CharField(max_length=120, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('address', models.CharField(max_length=300)),
                ('mobilenum', models.IntegerField(max_length=15)),
                ('emailid', models.CharField(max_length=150, unique=True)),
                ('username', models.CharField(max_length=150, unique=True)),
                ('password', models.CharField(max_length=150)),
                ('isActive', models.ImageField(max_length=2, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=150)),
                ('price', models.IntegerField(max_length=100)),
                ('quantity', models.IntegerField(max_length=150)),
                ('ram', models.CharField(max_length=150)),
                ('product_code', models.CharField(max_length=120, unique=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Product.Brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Product.Category')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Product.Color')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('product_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Product.Product')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Product.Users')),
            ],
        ),
    ]