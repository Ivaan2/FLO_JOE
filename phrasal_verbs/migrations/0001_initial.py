# Generated by Django 4.0 on 2022-08-12 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PhrasalVerb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verb', models.CharField(max_length=200)),
                ('definition', models.TextField(max_length=200)),
                ('traduction', models.TextField(max_length=200)),
                ('example', models.TextField(max_length=200)),
            ],
        ),
    ]