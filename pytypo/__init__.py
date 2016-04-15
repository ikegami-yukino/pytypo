# -*- coding: utf-8 -*-
"""pytypo - Spell correction

This module corrects spelling mistake.
That feature is based on TYPO CORPUS (http://luululu.com/tweet/)

And this module normalizes also lengthened English expression having repeating letters.
(e.g., this module converts "cooooooooooooooollllllllllllll" to "cool")

That feature is based on the following paper:
Samuel Brody and Nicholas Diakopoulos.
Cooooooooooooooollllllllllllll!!!!!!!!!!!!!! using word lengthening to detect sentiment in microblogs.
In EMNLP2011, pp. 562-570, 2011.
http://aclweb.org/anthology//D/D11/D11-1052.pdf


Author:
    Yukino Ikegami

Lisence:
    MIT License

Usage:
    import pytypo
    text = pytypo.correct(text) # Normalization for a word
    text = pytypo.normalize_sentence(text) # Normalization for a sentence
"""
from . import pytypo

VERSION = (0, 2, 0)
__version__ = '0.2.0'
__all__ = ['correct', 'correct_sentence', 'cut_repeat']

correct = pytypo.correct
correct_sentence = pytypo.correct_sentence
cut_repeat = pytypo.cut_repeat
