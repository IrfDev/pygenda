# Generated by Django 4.2.7 on 2023-11-10 08:12

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="contact",
            old_name="contacts",
            new_name="user",
        ),
    ]
