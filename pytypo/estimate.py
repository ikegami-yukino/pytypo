# -*- coding: utf-8 -*-
# This code is based on http://norvig.com/spell-correct.html
import bz2
import json
import os
import pkgutil

alphabet = 'abcdefghijklmnopqrstuvwxyz'
voca = json.loads(pkgutil.get_data('pytypo', os.path.join('voca.json')).decode('utf8'))


def edits1(word):
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [a + b[1:] for a, b in splits if b]
    transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b) > 1]
    replaces = [a + c + b[1:] for a, b in splits for c in alphabet if b]
    inserts = [a + c + b for a, b in splits for c in alphabet]
    return set(deletes + transposes + replaces + inserts)


def known_edits2(word):
    return set(e2 for e1 in edits1(word) for e2 in edits1(e1) if e2 in voca)


def known(words):
    return set(w for w in words if w in voca)


def estimate(word):
    candidates = (known([word]) or known(edits1(word))
            or known_edits2(word) or [word])
    return max(candidates, key=voca.get)
