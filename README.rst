Hangul romanization tool
~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://travis-ci.org/youknowone/hangul-romanize.svg?branch=master
    :target: https://travis-ci.org/youknowone/hangul-romanize

You can install the package from PyPI

    $ pip install hangul-romanize


Example
-------

Prelude::
    >>> from hangul_romanize import Transliter
    >>> from hangul_romanize.rule import academic
    >>>
    >>> transliter = Transliter(academic)
    >>> print(transliter.translit(u'안녕하세요'))
    annyeonghase-yo
