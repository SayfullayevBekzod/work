# Generated by Django 5.0.3 on 2024-03-22 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ish", "0004_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="fullname",
            field=models.CharField(default=1, max_length=128),
            preserve_default=False,
        ),
    ]
