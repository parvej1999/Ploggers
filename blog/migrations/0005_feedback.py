# Generated by Django 3.0.7 on 2020-10-11 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200620_0940'),
    ]

    operations = [
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(max_length=150)),
                ('contact', models.CharField(max_length=150)),
                ('msg', models.CharField(max_length=300)),
            ],
        ),
    ]
