# Generated by Django 4.1.5 on 2023-05-09 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0003_remove_experience_exp_time_experience_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_time', models.DurationField()),
                ('school', models.CharField(max_length=200)),
            ],
        ),
    ]
