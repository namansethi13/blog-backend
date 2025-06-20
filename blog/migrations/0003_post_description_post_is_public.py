# Generated by Django 5.2.3 on 2025-06-12 10:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0002_alter_section_alt_text_alter_section_content_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="description",
            field=models.TextField(default="no description available"),
        ),
        migrations.AddField(
            model_name="post",
            name="is_public",
            field=models.BooleanField(default=False),
        ),
    ]
