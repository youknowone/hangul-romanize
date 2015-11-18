# -*- coding: utf-8 -*-
from hangul_romanize.core import Syllable, Transliter
from hangul_romanize.rule import academic, REVISED_INITIALS, REVISED_VOWELS, REVISED_FINALS

import pytest


def test_const():
    assert len(REVISED_INITIALS) == 19
    assert len(REVISED_VOWELS) == 21
    assert len(REVISED_FINALS) == 28


@pytest.mark.parametrize(("input", "expected"), [
    (u'가', 'ga'),
    (u'힣', 'hih'),
    (u'밝', 'balg'),
])
def test_academic_rule(input, expected):
    try:
        s = Syllable(input)
    except:
        s = None
    output = academic((input, s), pre=(None, None))
    assert output == expected


@pytest.mark.parametrize(("input", "expected"), [
    (u'가', 'ga'),
    (u'힣', 'hih'),
    (u'밝', 'balg'),
    (u'밯망희', 'bahmanghui'),
    (u'안녕하세요', 'annyeonghase-yo'),
    (u'집', 'jib'),
    (u'짚', 'jip'),
    (u'밖', 'bakk'),
    (u'값', 'gabs'),
    (u'붓꽃', 'buskkoch'),
    (u'먹는', 'meogneun'),
    (u'독립', 'doglib'),
    (u'문리', 'munli'),
    (u'물엿', 'mul-yeos'),
    (u'굳이', 'gud-i'),
    (u'좋다', 'johda'),
    (u'가곡', 'gagog'),
    (u'조랑말', 'jolangmal'),
    (u'없었습니다', 'eobs-eoss-seubnida'),
    (u'띄고 문장부호! 있고!? @#())$#@()', u'ttuigo munjangbuho! issgo!? @#())$#@()'),
])
def test_academic(input, expected):
    transliter = Transliter(academic)
    output = transliter.translit(input)
    assert(output == expected)
