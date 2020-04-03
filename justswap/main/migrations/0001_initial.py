# -*- coding: utf-8 -*-
# Generated by Django 2.2.7 on 2019-11-24 11:01

from django.db import migrations, models


class Migration(migrations.Migration):
    """Initial migration that creates the example BlogPost model."""

    initial = True
    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BlogPost",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=80)),
                ("body", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modifiet_at", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
