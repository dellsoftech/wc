# Generated by Django 4.2.4 on 2023-09-26 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kg', '0021_g4level_g4_complexw_q_l1_g4level_g4_complexw_q_l2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kgtext',
            name='grade',
        ),
    ]
