# Generated by Django 4.2.6 on 2023-10-14 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nearest_bank_api', '0006_remove_atmservicethrough_workload_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='user_id',
            field=models.IntegerField(null=True, verbose_name='id пользователя'),
        ),
    ]
