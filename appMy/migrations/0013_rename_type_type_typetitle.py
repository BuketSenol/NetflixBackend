# Generated by Django 4.2.2 on 2023-07-26 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0012_rename_typetitle_type_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='type',
            old_name='type',
            new_name='typetitle',
        ),
    ]
