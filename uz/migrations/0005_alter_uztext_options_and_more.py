# Generated by Django 4.2.4 on 2023-10-10 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uz', '0004_alter_uztext_book_author_alter_uztext_book_title_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='uztext',
            options={'verbose_name': 'Текст на узбекском', 'verbose_name_plural': 'Тексты на узбекском'},
        ),
        migrations.AlterField(
            model_name='uztext',
            name='all_compound_words_p',
            field=models.FloatField(blank=True, null=True, verbose_name='% Сложных слов '),
        ),
        migrations.AlterField(
            model_name='uztext',
            name='complex_w_q',
            field=models.FloatField(blank=True, null=True, verbose_name='Количество составных слов'),
        ),
        migrations.AlterField(
            model_name='uztext',
            name='compound_w_q',
            field=models.FloatField(blank=True, null=True, verbose_name='Количество сложных и с тире слов '),
        ),
        migrations.AlterField(
            model_name='uztext',
            name='fw_p',
            field=models.FloatField(blank=True, null=True, verbose_name='% Часто испольщуемых слов'),
        ),
        migrations.AlterField(
            model_name='uztext',
            name='fw_q',
            field=models.FloatField(blank=True, null=True, verbose_name='Часто используемые слова'),
        ),
        migrations.AlterField(
            model_name='uztext',
            name='level_result',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Рекомендуемый класс'),
        ),
        migrations.AlterField(
            model_name='uztext',
            name='multisyllabic_wq',
            field=models.FloatField(blank=True, null=True, verbose_name='Многосложные слова'),
        ),
        migrations.AlterField(
            model_name='uztext',
            name='rareword_p',
            field=models.FloatField(blank=True, null=True, verbose_name='% Редких слов'),
        ),
        migrations.AlterField(
            model_name='uztext',
            name='rareword_q',
            field=models.FloatField(blank=True, null=True, verbose_name='Количество редких слов'),
        ),
        migrations.AlterField(
            model_name='uztext',
            name='syllables_avg',
            field=models.FloatField(blank=True, null=True, verbose_name='Средняя длина слов в слогах'),
        ),
        migrations.AlterField(
            model_name='uztext',
            name='uniq_w',
            field=models.IntegerField(blank=True, null=True, verbose_name='Количество уникальных слов'),
        ),
    ]
