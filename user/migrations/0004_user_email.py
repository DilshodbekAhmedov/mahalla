# Generated by Django 4.1.7 on 2023-02-24 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0003_alter_user_neighborhood_alter_user_sector"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="email",
            field=models.EmailField(blank=True, max_length=254, verbose_name="Почта"),
        ),
    ]
