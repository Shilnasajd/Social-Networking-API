# Generated by Django 5.0.6 on 2024-06-14 18:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_friendrequest_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='friendrequest',
            unique_together={('from_user', 'to_user')},
        ),
    ]
