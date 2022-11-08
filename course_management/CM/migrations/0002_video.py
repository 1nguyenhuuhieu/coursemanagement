# Generated by Django 4.1.3 on 2022-11-07 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CM', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('descreption', models.CharField(max_length=1000)),
                ('url', models.FileField(upload_to='')),
                ('course', models.ManyToManyField(to='CM.course')),
            ],
        ),
    ]
