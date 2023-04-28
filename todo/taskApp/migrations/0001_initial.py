# Generated by Django 4.2 on 2023-04-26 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='taskModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=500)),
                ('complete', models.BooleanField(default=False)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]