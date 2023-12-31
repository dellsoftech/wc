# Generated by Django 4.2.4 on 2023-10-10 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uz', '0003_rename_kgtext_uztext'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uztext',
            name='book_author',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='uztext',
            name='book_title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Название произведения'),
        ),
        migrations.AlterField(
            model_name='uztext',
            name='words_q',
            field=models.IntegerField(blank=True, null=True, verbose_name='Количество слов'),
        ),
    ]
