# -*- coding: utf-8 -*-
from sys import version_info
import re
from . import _conv_table

re_symbol = re.compile("[^a-zA-Z0-9']{2,256}$")

if version_info < (3, 0, 0):
    range = xrange


def cut_repeat(text, threshold):
    """Reduce repeated characters until threshold
    Param:
        <str> text
        <int> threshold
    Return:
        <str> result
    """
    text = list(text)
    result = text[0]
    count = 0
    for i in range(1, len(text)):
        if text[i - 1] == text[i]:
            count += 1
            if count < threshold:
                result += text[i]
        else:
            count = 0
            result += text[i]
    return result


def correct(word):
    """Normalize repeat expression for English
    Param:
        <str> word
    Return:
        <str> normalized_word
    """
    suffix_symbol = re_symbol.findall(word)
    if suffix_symbol:
        word = word.replace(suffix_symbol[0], '')
    word = cut_repeat(word, 2)
    normalized_word = _conv_table.eng_lengthened.get(word, word)
    if normalized_word == word:
        normalized_word = _conv_table.eng_typo.get(word, word)
    if suffix_symbol:
        return (normalized_word + cut_repeat(suffix_symbol[0], 1))
    return normalized_word


def correct_sentence(sentence):
    """Normalize for each word
    Param:
        <str> sentence
    Return:
        <str> normalized_sentence
    """
    return ' '.join([correct(word) for word in sentence.split()])
