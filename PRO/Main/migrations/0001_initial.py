# Generated by Django 4.0.2 on 2022-06-20 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('job_title', models.CharField(max_length=50)),
                ('date_of_receipt', models.DateField()),
                ('salary', models.IntegerField()),
                ('head', models.IntegerField()),
            ],
            options={
                'db_table': 'Employees',
            },
        ),
    ]
