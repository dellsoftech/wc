# Generated by Django 4.2.4 on 2023-09-11 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kg', '0020_rename_g4_longw_q_l1_g4level_g4_multisyllabic_wq_l1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='g4level',
            name='g4_complexw_q_l1',
            field=models.FloatField(blank=True, null=True, verbose_name='Кошмок сөздөрдүн саны 4.1'),
        ),
        migrations.AddField(
            model_name='g4level',
            name='g4_complexw_q_l2',
            field=models.FloatField(blank=True, null=True, verbose_name='Кошмок сөздөрдүн саны 4.2'),
        ),
    ]
