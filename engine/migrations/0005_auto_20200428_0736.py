# Generated by Django 3.0.5 on 2020-04-28 04:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0004_choice_question'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]