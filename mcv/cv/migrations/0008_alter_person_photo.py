# Generated by Django 4.1.5 on 2023-05-09 18:19

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0007_alter_person_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='photo',
            field=sorl.thumbnail.fields.ImageField(upload_to=''),
        ),
    ]