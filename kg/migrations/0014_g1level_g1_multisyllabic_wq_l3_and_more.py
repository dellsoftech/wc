# Generated by Django 4.2.4 on 2023-09-11 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kg', '0013_rename_g1_longw_q_l3_g1level_g1_multisyllabic_wq_l2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='g1level',
            name='g1_multisyllabic_wq_l3',
            field=models.FloatField(blank=True, null=True, verbose_name='Многосложные  слова 1.3'),
        ),
        migrations.AlterField(
            model_name='g1level',
            name='g1_multisyllabic_wq_l2',
            field=models.FloatField(blank=True, null=True, verbose_name='Многосложные  слова 1.2'),
        ),
    ]
