# Generated by Django 4.1 on 2022-09-13 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=16)),
                ('model', models.CharField(max_length=16)),
                ('color', models.CharField(max_length=16)),
                ('condition', models.CharField(max_length=16)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ManyImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(max_length=255, upload_to='inside_img')),
                ('item_images', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_images', to='item.item')),
            ],
        ),
    ]