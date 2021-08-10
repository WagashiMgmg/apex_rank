# Generated by Django 2.2.24 on 2021-08-10 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210810_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='sample_4',
            field=models.FloatField(blank=True, null=True, verbose_name='平均ダメージ, average damage'),
        ),
        migrations.AlterField(
            model_name='item',
            name='sample_5',
            field=models.FloatField(blank=True, null=True, verbose_name='K/D'),
        ),
        migrations.AlterField(
            model_name='item',
            name='sample_6',
            field=models.BooleanField(verbose_name='神に誓って嘘が無い場合はチェックを入れる'),
        ),
        migrations.AlterField(
            model_name='item',
            name='sample_9',
            field=models.IntegerField(blank=True, choices=[('B4', 'ブロンズ4, B4'), ('B3', 'ブロンズ3, B3'), ('B2', 'ブロンズ2, B2'), ('B1', 'ブロンズ1, B1'), ('S4', 'シルバー4, S4'), ('S3', 'シルバー3, S3'), ('S2', 'シルバー2, S2'), ('S1', 'シルバー1, S1'), ('G4', 'ゴールド4, G4'), ('G3', 'ゴールド3, G3'), ('G2', 'ゴールド2, G2'), ('G1', 'ゴールド1, G1'), ('P4', 'プラチナ4, P4'), ('P3', 'プラチナ3, P3'), ('P2', 'プラチナ2, P2'), ('P1', 'プラチナ1, P1'), ('D4', 'ダイア4, D4'), ('D3', 'ダイア3, D3'), ('D2', 'ダイア2, D2'), ('D1', 'ダイア1, D1'), ('MA', 'マスター, Master'), ('PR', 'プレデター, predator')], null=True, verbose_name='ランク(rank)'),
        ),
    ]