# -*- coding: utf-8 -*-

try:
    unicode(0)
except NameError:
    # py3
    unicode = str
    unichr = chr


class Syllable(object):
    """Hangul syllable interface"""

    MIN = ord(u'가')
    MAX = ord(u'힣')

    def __init__(self, char=None, code=None):
        if char is None and code is None:
            raise TypeError('__init__ takes char or code as a keyword argument (not given)')
        if char is not None and code is not None:
            raise TypeError('__init__ takes char or code as a keyword argument (both given)')
        if char:
            code = ord(char)
        if not self.MIN <= code <= self.MAX:
            raise TypeError('__init__ expected Hangul syllable but {0} not in [{1}..{2}]'.format(code, self.MIN, self.MAX))
        self.code = code

    @property
    def index(self):
        return self.code - self.MIN

    @property
    def initial(self):
        return self.index // 588

    @property
    def vowel(self):
        return (self.index // 28) % 21

    @property
    def final(self):
        return self.index % 28

    @property
    def char(self):
        return unichr(self.code)

    def __unicode__(self):
        return self.char

    def __repr__(self):
        return u'''<Syllable({}({}),{}({}),{}({}),{}({}))>'''.format(
            self.code, self.char, self.initial, u'', self.vowel, u'', self.final, u'')


class Transliter(object):
    """General transliting interface"""

    def __init__(self, rule):
        self.rule = rule

    def translit(self, text):
        """Translit text to romanized text

        :param text: Unicode string or unicode character iterator
        """
        result = []
        pre = None, None
        now = None, None
        for c in text:
            try:
                post = c, Syllable(c)
            except TypeError:
                post = c, None

            if now[0] is not None:
                out = self.rule(now, pre=pre, post=post)
                if out is not None:
                    result.append(out)

            pre = now
            now = post

        if now is not None:
            out = self.rule(now, pre=pre, post=(None, None))
            if out is not None:
                result.append(out)

        return u''.join(result)
