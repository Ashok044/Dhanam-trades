# Generated by Django 4.1.7 on 2023-03-18 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('desc', models.TextField()),
                ('image', models.ImageField(upload_to='pics/')),
                ('trending', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Design',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(null=True, upload_to='pics/')),
                ('desc', models.TextField(null=True)),
                ('name', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=30)),
                ('cnumber', models.IntegerField()),
                ('cproducts', models.TextField()),
                ('ccost', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=30)),
                ('pdesc', models.TextField()),
                ('pimage', models.ImageField(upload_to='pics/')),
                ('ptrending', models.BooleanField(default=False)),
                ('key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.category')),
            ],
        ),
    ]
