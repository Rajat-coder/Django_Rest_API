# Generated by Django 3.1.4 on 2020-12-11 12:09

from django.db import migrations, models
import myapp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Employee_id', models.CharField(max_length=10, unique=True)),
                ('Name', models.CharField(max_length=10)),
                ('Age', models.IntegerField()),
                ('Rank', models.FloatField()),
                ('Photo', models.ImageField(blank=True, null=True, upload_to=myapp.models.User.upload_photo)),
                ('Resume', models.ImageField(blank=True, null=True, upload_to=myapp.models.User.upload_file)),
            ],
        ),
    ]