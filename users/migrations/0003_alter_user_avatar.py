# Generated by Django 5.1.6 on 2025-02-24 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_alter_user_avatar"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="avatar",
            field=models.ImageField(
                blank=True,
                help_text="Загрузите фото",
                null=True,
                upload_to="avatars/",
                verbose_name="Аватар",
            ),
        ),
    ]
