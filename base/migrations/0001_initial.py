# Generated by Django 4.2.1 on 2023-05-20 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('company', models.CharField(max_length=255)),
                ('logo', models.ImageField(upload_to='logos/')),
                ('new', models.BooleanField(default=False)),
                ('featured', models.BooleanField(default=False)),
                ('position', models.CharField(max_length=255)),
                ('role', models.CharField(max_length=255)),
                ('level', models.CharField(max_length=255)),
                ('postedAt', models.DateTimeField()),
                ('contract', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('languages', models.CharField(max_length=255)),
                ('tools', models.CharField(max_length=255)),
            ],
        ),
    ]
