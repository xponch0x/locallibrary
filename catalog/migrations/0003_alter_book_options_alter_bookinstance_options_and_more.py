# Generated by Django 5.0.2 on 2024-04-03 20:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0002_language"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="book",
            options={"ordering": ["title", "author"]},
        ),
        migrations.AlterModelOptions(
            name="bookinstance",
            options={
                "ordering": ["due_back"],
                "permissions": (("can_mark_returned", "Set book as returned"),),
            },
        ),
        migrations.RemoveConstraint(
            model_name="genre",
            name="genre_name_case_insensitive_unique",
        ),
        migrations.AddField(
            model_name="book",
            name="language",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="catalog.language",
            ),
        ),
        migrations.AddField(
            model_name="bookinstance",
            name="borrower",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="author",
            name="date_of_death",
            field=models.DateField(blank=True, null=True, verbose_name="died"),
        ),
        migrations.AlterField(
            model_name="bookinstance",
            name="status",
            field=models.CharField(
                blank=True,
                choices=[
                    ("d", "Maintenance"),
                    ("o", "On loan"),
                    ("a", "Available"),
                    ("r", "Reserved"),
                ],
                default="d",
                help_text="Book availability",
                max_length=1,
            ),
        ),
    ]
