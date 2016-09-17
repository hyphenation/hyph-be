#!/usr/bin/python3
#
# Copyright (c) 2016 Maksim Salau <maksim.salau@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom
# the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
# OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import fileinput

L = list("аеёіоуыэюяўй")

rules = list()

def has_letters_from_L(word):
    for s in word:
        if s in L:
            return True
    return False

def process(word):
    if len(word) < 5:
        return
    # 2 consonants at the beginning of a word followed by a quote
    # There is no need for rules for 3 consonants, since hyphenation
    # between the third consonant and subsequent vowel is not allowed anyway
    s = word[:3]
    if s.endswith("'") and not has_letters_from_L(s):
        rule = ".{0}8".format(s)
        if rule not in rules:
            rules.append(rule)
            print(rule)
    # 3 consonants at the end of a word
    # or 2 consonants followed by a soft sign
    # If the soft sign appears before 2 consonants,
    # this case is handled by rules for 2 consonants.
    # When the soft sign appears in between consonants, hyphenation
    # of the last consonants is handled by righthyphenmin=2 and hyphenation
    # before the consonants preceding the soft sign is handled
    # by the rules for the soft sign: 6Cь1C. + 8C. => 6Cь8C.
    s = word[-3:]
    if ("ь" not in s[:2]) and not has_letters_from_L(s):
        rule = "8{0}.".format(s)
        if rule not in rules:
            rules.append(rule)
            print(rule)

with fileinput.input() as f:
    for line in f:
        process(line.strip().lower())
