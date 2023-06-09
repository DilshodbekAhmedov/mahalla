# Generated by Django 4.1.7 on 2023-02-26 08:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("mahalla", "0005_remove_neighborhood_leader_remove_sector_leader"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="citizen",
            options={
                "ordering": ("id",),
                "verbose_name": "Fuqaro",
                "verbose_name_plural": "Fuqarolar",
            },
        ),
        migrations.AlterModelOptions(
            name="neighborhood",
            options={
                "ordering": ("id",),
                "verbose_name": "Mahalla",
                "verbose_name_plural": "Mahallalar",
            },
        ),
        migrations.AlterModelOptions(
            name="sector",
            options={
                "ordering": ("id",),
                "verbose_name": "Sektor",
                "verbose_name_plural": "Sektrlar",
            },
        ),
    ]
