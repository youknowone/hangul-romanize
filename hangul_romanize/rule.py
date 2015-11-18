# -*- coding: utf-8 -*-

REVISED_INITIALS = 'g', 'kk', 'n', 'd', 'tt', 'l', 'm', 'b', 'pp', 's', 'ss', '', 'j', 'jj', 'ch', 'k', 't', 'p', 'h'
REVISED_VOWELS = 'a', 'ae', 'ya', 'yae', 'eo', 'e', 'yeo', 'ye', 'o', 'wa', 'wae', 'oe', 'yo', 'u', 'wo', 'we', 'wi', 'yu', 'eu', 'ui', 'i'
REVISED_FINALS = '', 'g', 'kk', 'gs', 'n', 'nj', 'nh', 'd', 'l', 'lg', 'lm', 'lb', 'ls', 'lt', 'lp', 'lh', 'm', 'b', 'bs', 's', 'ss', 'ng', 'j', 'ch', 'k', 't', 'p', 'h'


def academic_ambiguous_patterns():
    import itertools
    result = set()
    for final, initial in itertools.product(REVISED_FINALS, REVISED_INITIALS):
        check = False
        combined = final + initial
        for i in range(len(combined)):
            head, tail = combined[:i], combined[i:]
            if head in REVISED_FINALS and tail in REVISED_INITIALS:
                if not check:
                    check = True
                else:
                    result.add(combined)
                    break
    return result


ACADEMIC_AMBIGUOUS_PATTERNS = academic_ambiguous_patterns()


def academic(now, pre, **options):
    """Rule for academic translition."""
    c, s = now
    if not s:
        return c

    ps = pre[1] if pre else None

    marker = False
    if ps:
        if s.initial == 11:
            marker = True
        elif ps and (REVISED_FINALS[ps.final] + REVISED_INITIALS[s.initial]) in ACADEMIC_AMBIGUOUS_PATTERNS:
            marker = True

    r = u''
    if marker:
        r += '-'
    r += REVISED_INITIALS[s.initial] + REVISED_VOWELS[s.vowel] + REVISED_FINALS[s.final]
    return r
