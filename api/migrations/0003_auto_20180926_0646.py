# Generated by Django 2.1.1 on 2018-09-26 06:46

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_kakaouser_context'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kakaouser',
            name='context',
            field=jsonfield.fields.JSONField(default={}),
        ),
    ]
