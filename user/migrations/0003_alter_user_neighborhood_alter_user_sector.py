# Generated by Django 4.1.7 on 2023-02-24 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("mahalla", "0005_remove_neighborhood_leader_remove_sector_leader"),
        ("user", "0002_remove_user_email_user_neighborhood_user_sector_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="neighborhood",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="mahalla.neighborhood",
                verbose_name="Qaysi mahalla rahbari",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="sector",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="mahalla.sector",
                verbose_name="Qaysi sektor rahbari",
            ),
        ),
    ]