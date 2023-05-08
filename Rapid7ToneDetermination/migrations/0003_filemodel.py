# Generated by Django 4.1.7 on 2023-03-31 02:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Rapid7ToneDetermination", "0002_alter_user_username"),
    ]

    operations = [
        migrations.CreateModel(
            name="FileModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=64)),
                ("path", models.CharField(max_length=128)),
                (
                    "uploadTime",
                    models.DateTimeField(
                        default=datetime.datetime(
                            2023, 3, 31, 2, 30, 8, 826113, tzinfo=datetime.timezone.utc
                        )
                    ),
                ),
            ],
        ),
    ]
