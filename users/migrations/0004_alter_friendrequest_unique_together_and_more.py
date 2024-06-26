# Generated by Django 5.0.6 on 2024-06-14 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_friendrequest'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='friendrequest',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='friendrequest',
            name='accepted',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
