# Generated by Django 4.2.2 on 2023-07-26 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0003_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='moviecard',
            old_name='type',
            new_name='movieType',
        ),
    ]