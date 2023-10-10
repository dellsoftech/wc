# Generated by Django 4.0.4 on 2023-06-02 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FreqWord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('freq_words', models.TextField(blank=True, null=True, verbose_name='Часто используемые слова')),
            ],
            options={
                'verbose_name': 'Список часто используемых слов',
                'verbose_name_plural': 'Часто используемые слова',
            },
        ),
        migrations.CreateModel(
            name='g1Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('g1_word_q_l1', models.IntegerField(blank=True, null=True, verbose_name='Кол-во слов для уровня 1.1')),
                ('g1_word_q_l2', models.IntegerField(blank=True, null=True, verbose_name='Кол-во слов для уровня 1.2')),
                ('g1_word_q_l3', models.IntegerField(blank=True, null=True, verbose_name='Кол-во слов для уровня 1.3')),
                ('g1_sentence_q_l1', models.FloatField(blank=True, null=True, verbose_name='Общее кол. предложений 1.1')),
                ('g1_sentence_q_l2', models.FloatField(blank=True, null=True, verbose_name='Общее кол. предложений 1.2')),
                ('g1_sentence_q_l3', models.FloatField(blank=True, null=True, verbose_name='Общее кол. предложений 1.3')),
                ('g1_avgwl_insyllables_l1', models.FloatField(blank=True, null=True, verbose_name='Ср. длина слова в слогах 1.1')),
                ('g1_avgwl_insyllables_l2', models.FloatField(blank=True, null=True, verbose_name='Ср. длина слова в слогах 1.2')),
                ('g1_avgwl_insyllables_l3', models.FloatField(blank=True, null=True, verbose_name='Ср. длина слова в слогах 1.3')),
                ('g1_avgl_sentences_inw_l1', models.FloatField(blank=True, null=True, verbose_name='Сред. дл. предл. в словах 1.1')),
                ('g1_avgl_sentences_inw_l2', models.FloatField(blank=True, null=True, verbose_name='Сред. дл. предл. в словах 1.2')),
                ('g1_avgl_sentences_inw_l3', models.FloatField(blank=True, null=True, verbose_name='Сред. дл. предл. в словах 1.3')),
                ('g1_longw_q_l1', models.FloatField(blank=True, null=True, verbose_name='Многосложные  слова 1.1')),
                ('g1_longw_q_l2', models.FloatField(blank=True, null=True, verbose_name='Многосложные  слова 1.2')),
                ('g1_longw_q_l3', models.FloatField(blank=True, null=True, verbose_name='Многосложные  слова 1.3')),
                ('g1_compw_q_l1', models.FloatField(blank=True, null=True, verbose_name='Кол-во сложных  слов 1.1')),
                ('g1_compw_q_l2', models.FloatField(blank=True, null=True, verbose_name='Кол-во сложных  слов 1.2')),
                ('g1_compw_q_l3', models.FloatField(blank=True, null=True, verbose_name='Кол-во сложных  слов 1.3')),
                ('g1_rarew_q_l1', models.FloatField(blank=True, null=True, verbose_name='Кол-во редких  слов 1.1')),
                ('g1_rarew_q_l2', models.FloatField(blank=True, null=True, verbose_name='Кол-во редких  слов 1.2')),
                ('g1_rarew_q_l3', models.FloatField(blank=True, null=True, verbose_name='Кол-во редких  слов 1.3')),
            ],
            options={
                'verbose_name': 'Уровень для 1-го класса',
                'verbose_name_plural': 'Уровни для 1-го класса',
            },
        ),
        migrations.CreateModel(
            name='g2Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('g2_word_q_l1', models.IntegerField(blank=True, null=True, verbose_name='Кол-во слов для уровня 2.1')),
                ('g2_word_q_l2', models.IntegerField(blank=True, null=True, verbose_name='Кол-во слов для уровня 2.2')),
                ('g2_sentence_q_l1', models.FloatField(blank=True, null=True, verbose_name='Общее кол. предложений 2.1')),
                ('g2_sentence_q_l2', models.FloatField(blank=True, null=True, verbose_name='Общее кол. предложений 2.2')),
                ('g2_avgwl_insyllables_l1', models.FloatField(blank=True, null=True, verbose_name='Ср. длина слова в слогах 2.1')),
                ('g2_avgwl_insyllables_l2', models.FloatField(blank=True, null=True, verbose_name='Ср. длина слова в слогах 2.2')),
                ('g2_avgl_sentences_inw_l1', models.FloatField(blank=True, null=True, verbose_name='Сред. дл. предл. в словах 2.1')),
                ('g2_avgl_sentences_inw_l2', models.FloatField(blank=True, null=True, verbose_name='Сред. дл. предл. в словах 2.2')),
                ('g2_longw_q_l1', models.FloatField(blank=True, null=True, verbose_name='Многосложные  слова 2.1')),
                ('g2_longw_q_l2', models.FloatField(blank=True, null=True, verbose_name='Многосложные  слова 2.2')),
                ('g2_compw_q_l1', models.FloatField(blank=True, null=True, verbose_name='Кол-во сложных  слов 2.1')),
                ('g2_compw_q_l2', models.FloatField(blank=True, null=True, verbose_name='Кол-во сложных  слов 2.2')),
                ('g2_rarew_q_l1', models.FloatField(blank=True, null=True, verbose_name='Кол-во редких  слов 2.1')),
                ('g2_rarew_q_l2', models.FloatField(blank=True, null=True, verbose_name='Кол-во редких  слов 2.2')),
            ],
            options={
                'verbose_name': 'Уровень для 2-го класса',
                'verbose_name_plural': 'Уровни для 2-го класса',
            },
        ),
        migrations.CreateModel(
            name='g3Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('g3_word_q_l1', models.IntegerField(blank=True, null=True, verbose_name='Кол-во слов для уровня 3.1')),
                ('g3_word_q_l2', models.IntegerField(blank=True, null=True, verbose_name='Кол-во слов для уровня 3.2')),
                ('g3_sentence_q_l1', models.FloatField(blank=True, null=True, verbose_name='Общее кол. предложений 3.1')),
                ('g3_sentence_q_l2', models.FloatField(blank=True, null=True, verbose_name='Общее кол. предложений 3.2')),
                ('g3_avgwl_insyllables_l1', models.FloatField(blank=True, null=True, verbose_name='Ср. длина слова в слогах 3.1')),
                ('g3_avgwl_insyllables_l2', models.FloatField(blank=True, null=True, verbose_name='Ср. длина слова в слогах 3.2')),
                ('g3_avgl_sentences_inw_l1', models.FloatField(blank=True, null=True, verbose_name='Сред. дл. предл. в словах 3.1')),
                ('g3_avgl_sentences_inw_l2', models.FloatField(blank=True, null=True, verbose_name='Сред. дл. предл. в словах 3.2')),
                ('g3_longw_q_l1', models.FloatField(blank=True, null=True, verbose_name='Многосложные  слова 3.1')),
                ('g3_longw_q_l2', models.FloatField(blank=True, null=True, verbose_name='Многосложные  слова 3.2')),
                ('g3_compw_q_l1', models.FloatField(blank=True, null=True, verbose_name='Кол-во сложных  слов 3.1')),
                ('g3_compw_q_l2', models.FloatField(blank=True, null=True, verbose_name='Кол-во сложных  слов 3.2')),
                ('g3_rarew_q_l1', models.FloatField(blank=True, null=True, verbose_name='Кол-во редких  слов 3.1')),
                ('g3_rarew_q_l2', models.FloatField(blank=True, null=True, verbose_name='Кол-во редких  слов 3.2')),
            ],
            options={
                'verbose_name': 'Уровень для 3-го класса',
                'verbose_name_plural': 'Уровни для 3-го класса',
            },
        ),
        migrations.CreateModel(
            name='g4Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('g4_word_q_l1', models.IntegerField(blank=True, null=True, verbose_name='Кол-во слов для уровня 4.1')),
                ('g4_word_q_l2', models.IntegerField(blank=True, null=True, verbose_name='Кол-во слов для уровня 4.2')),
                ('g4_sentence_q_l1', models.FloatField(blank=True, null=True, verbose_name='Общее кол. предложений 4.1')),
                ('g4_sentence_q_l2', models.FloatField(blank=True, null=True, verbose_name='Общее кол. предложений 4.2')),
                ('g4_avgwl_insyllables_l1', models.FloatField(blank=True, null=True, verbose_name='Ср. длина слова в слогах 4.1')),
                ('g4_avgwl_insyllables_l2', models.FloatField(blank=True, null=True, verbose_name='Ср. длина слова в слогах 4.2')),
                ('g4_avgl_sentences_inw_l1', models.FloatField(blank=True, null=True, verbose_name='Сред. дл. предл. в словах 4.1')),
                ('g4_avgl_sentences_inw_l2', models.FloatField(blank=True, null=True, verbose_name='Сред. дл. предл. в словах 4.2')),
                ('g4_longw_q_l1', models.FloatField(blank=True, null=True, verbose_name='Многосложные  слова 4.1')),
                ('g4_longw_q_l2', models.FloatField(blank=True, null=True, verbose_name='Многосложные  слова 4.2')),
                ('g4_compw_q_l1', models.FloatField(blank=True, null=True, verbose_name='Кол-во сложных  слов 4.1')),
                ('g4_compw_q_l2', models.FloatField(blank=True, null=True, verbose_name='Кол-во сложных  слов 4.2')),
                ('g4_rarew_q_l1', models.FloatField(blank=True, null=True, verbose_name='Кол-во редких  слов 4.1')),
                ('g4_rarew_q_l2', models.FloatField(blank=True, null=True, verbose_name='Кол-во редких  слов 4.2')),
            ],
            options={
                'verbose_name': 'Уровень для 4-го класса',
                'verbose_name_plural': 'Уровни для 4-го класса',
            },
        ),
        migrations.CreateModel(
            name='LCWord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lc_words', models.TextField(blank=True, null=True, verbose_name='Длинные и сложные слова для 1-4 класса')),
            ],
            options={
                'verbose_name': 'Список сложных слов для 1-4 класса',
                'verbose_name_plural': 'Сложные слова для 1-4 класса',
            },
        ),
        migrations.CreateModel(
            name='RareWord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rare_words', models.TextField(blank=True, null=True, verbose_name='Редко используемые  слова')),
            ],
            options={
                'verbose_name': 'Список редко используемых слов для 1-4 класса',
                'verbose_name_plural': 'Редкие слова для 1-4 класса',
            },
        ),
        migrations.CreateModel(
            name='uzText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.IntegerField(blank=True, null=True, verbose_name='Класс')),
                ('book_title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название произведения')),
                ('book_author', models.CharField(blank=True, max_length=255, null=True, verbose_name='Автор')),
                ('book_text', models.TextField(blank=True, null=True, verbose_name='Текст')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('words_q', models.IntegerField(blank=True, null=True, verbose_name='Кол-во слов')),
                ('sentence_q', models.IntegerField(blank=True, null=True, verbose_name='Кол-во предложений')),
                ('syllables_avg', models.FloatField(blank=True, null=True, verbose_name='Ср. длина слова в слогах')),
                ('sentence_avg', models.FloatField(blank=True, null=True, verbose_name='Сред. кол-во слов в предлож.')),
                ('longw_q', models.FloatField(blank=True, null=True, verbose_name='Кол-во многосложных слов')),
                ('lcwords_q', models.FloatField(blank=True, null=True, verbose_name='Кол-во сложных  слов для 1-4 кл.')),
                ('lcwords_p', models.FloatField(blank=True, null=True, verbose_name='% Сложных  слов для 1-4 кл.')),
                ('rareword_q', models.FloatField(blank=True, null=True, verbose_name='Кол-во редких  слов для 1-4 кл.')),
                ('rareword_p', models.FloatField(blank=True, null=True, verbose_name='% редких  слов для 1-4 кл.')),
                ('fw_q', models.FloatField(blank=True, null=True, verbose_name='Часто используемые слова')),
                ('fw_p', models.FloatField(blank=True, null=True, verbose_name='% часто используемых слов')),
                ('uniq_w', models.IntegerField(blank=True, null=True, verbose_name='Кол-во уник-ых слов')),
                ('lexical_div', models.FloatField(blank=True, null=True, verbose_name='Коэф. лекс-го разн-ия')),
                ('level_result', models.CharField(blank=True, max_length=255, null=True, verbose_name='Рекемендуемый класс')),
            ],
            options={
                'verbose_name': 'Текст на узбекском',
                'verbose_name_plural': 'Тексты на узбекском',
            },
        ),
    ]
