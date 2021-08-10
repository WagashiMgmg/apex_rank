from django import template
from math import modf
register = template.Library()

@register.filter(name="int_rank")
def int_rank(rank):
    sample_9_choice = (
        (0, 'ブロンズ4, B4'),
        (1, 'ブロンズ3, B3'),
        (2, 'ブロンズ2, B2'),
        (3, 'ブロンズ1, B1'),
        (4, 'シルバー4, S4'),
        (5, 'シルバー3, S3'),
        (6, 'シルバー2, S2'),
        (7, 'シルバー1, S1'),
        (8, 'ゴールド4, G4'),
        (9, 'ゴールド3, G3'),
        (10, 'ゴールド2, G2'),
        (11, 'ゴールド1, G1'),
        (12, 'プラチナ4, P4'),
        (13, 'プラチナ3, P3'),
        (14, 'プラチナ2, P2'),
        (15, 'プラチナ1, P1'),
        (16, 'ダイア4, D4'),
        (17, 'ダイア3, D3'),
        (18, 'ダイア2, D2'),
        (19, 'ダイア1, D1'),
        (20, 'マスター, Master'),
        (21,'プレデター, predator'),
        )
    return sample_9_choice[rank][1]