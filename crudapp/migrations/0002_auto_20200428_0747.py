# Generated by Django 2.2.12 on 2020-04-28 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeemodel',
            name='id',
        ),
        migrations.AlterField(
            model_name='employeemodel',
            name='eid',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]