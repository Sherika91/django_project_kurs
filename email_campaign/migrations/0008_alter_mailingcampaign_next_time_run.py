# Generated by Django 4.2.4 on 2023-10-01 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('email_campaign', '0007_alter_mailingcampaign_mail_clients_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailingcampaign',
            name='next_time_run',
            field=models.DateTimeField(default=None, null=True, verbose_name='Next time run'),
        ),
    ]
