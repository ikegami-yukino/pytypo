pytypo
===========
|travis| |coveralls| |landscape| |downloads| |pyversion| |version| |license|

pytypo corrects English spelling mistakes.
That feature is based on TYPO CORPUS (http://luululu.com/tweet/)

And this module normalizes also lengthened English expression having repeating letters.
(e.g., this module converts "cooooooooooooooollllllllllllll" to "cool")

That feature is based on the following paper:
Samuel Brody and Nicholas Diakopoulos.
Cooooooooooooooollllllllllllll!!!!!!!!!!!!!! using word lengthening to detect sentiment in microblogs.
In EMNLP2011, pp. 562-570, 2011.
http://aclweb.org/anthology//D/D11/D11-1052.pdf


Contributions are welcome!


Installation
============

::

 $ pip install pytypo


Usage
=====

Import pytypo
--------------------------------------------

::

 >>> import pytypo


correct sentence
--------------------------------------------

::

 >>> pytypo.correct_sentence('you are coooolll!!!')
 you are cool!


- correct_sentence(str)


correct word
--------------------------------------------

::

 >>> pytypo.correct('okayyyyy')
 okay


- correct(str)


Shorten repeated substring until threshould without dictionary
-------------------------------------------------------------------

::

 >>> pytypo.cut_repeat('mamisaaaaaan', 1)
 mamisan
 >>> pytypo.cut_repeat('okayyyyy', 2)
 okayy


- cut_repeat(str, threshould)

  * Note that this method don't use a lengthened expression normalize table (e.g., cooll -> cool).
    If you want to normalize such expression, use `correct()` or `correct_sentence()` method.

License
=========

- This module is licensed under MIT License.

.. |travis| image:: https://travis-ci.org/ikegami-yukino/pytypo.svg?branch=master
    :target: https://travis-ci.org/ikegami-yukino/pytypo
    :alt: travis-ci.org

.. |coveralls| image:: https://coveralls.io/repos/ikegami-yukino/pytypo/badge.svg?branch=master&service=github
    :target: https://coveralls.io/github/ikegami-yukino/pytypo?branch=master
    :alt: coveralls.io

.. |landscape| image:: https://landscape.io/github/ikegami-yukino/pytypo/master/landscape.svg?style=flat
   :target: https://landscape.io/github/ikegami-yukino/pytypo/master
   :alt: Code Health

.. |downloads| image:: https://img.shields.io/pypi/dm/pytypo.svg
    :target: http://pypi.python.org/pypi/pytypo/
    :alt: downloads

.. |pyversion| image:: https://img.shields.io/pypi/pyversions/pytypo.svg

.. |version| image:: https://img.shields.io/pypi/v/pytypo.svg
    :target: http://pypi.python.org/pypi/pytypo/
    :alt: latest version

.. |license| image:: https://img.shields.io/pypi/l/pytypo.svg
    :target: http://pypi.python.org/pypi/pytypo/
    :alt: license
