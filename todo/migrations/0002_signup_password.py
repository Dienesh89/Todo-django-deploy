# Generated by Django 4.1.7 on 2023-03-05 04:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("todo", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="signup",
            name="password",
            field=models.CharField(default="not set earlier", max_length=12),
            preserve_default=False,
        ),
    ]
