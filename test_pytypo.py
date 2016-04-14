# -*- coding: utf-8 -*-
from nose.tools import assert_equal
import pytypo


def test_cut_repeat():
    assert_equal(pytypo.cut_repeat('pytypooooooo', 1), 'pytypo')
    assert_equal(pytypo.cut_repeat('beeeeer', 2), 'beer')


def test_correct():
    # TYPO CORPUS
    assert_equal(pytypo.correct('twiter'), 'twitter')
    # estimate by Wikipedia article titles
    assert_equal(pytypo.correct('speling'), 'spelling')
    # lengthned words
    assert_equal(pytypo.correct('thanxxxx'), 'thanx')
    assert_equal(pytypo.correct('coooooooolllll!!!!'), 'cool!')


def test_correct_sentence():
    normalized = pytypo.correct_sentence('you are coooolll!!!')
    assert_equal(normalized, 'you are cool!')
