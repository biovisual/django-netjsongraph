# Generated by Django 2.2.9 on 2019-12-24 07:52

import jsonfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_netjsongraph', '0007_link_status_changed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='node', old_name='addresses', new_name='addresses_old',
        ),
        migrations.AddField(
            model_name='node',
            name='addresses',
            field=jsonfield.fields.JSONField(default=[]),
        ),
    ]
