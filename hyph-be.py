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

from itertools import product

C = list("бвгґджзклмнпрстфхцчш")
V = list("аеёіоуыэюя")
K = list("йў")
A = list("'")
M = list("ь")
HC = list('джртчш') # hard-only consonants

header = """% Created by: TBD
% License: TBD
%
% Створана адпаведна правілаў, зацверджаных законам
% ад 23 лiпеня 2008 г. No 420-З
% Аб Правiлах беларускай арфаграфii i пунктуацыi
% http://academy.edu.by/files/zak_420-3.pdf
%
% РАЗДЗЕЛ I. АРФАГРАФIЯ
% ГЛАВА 8 ПРАВIЛЫ ПЕРАНОСУ
% § 41. Правiлы пераносу простых, складаных, складанаскарочаных слоў,
%       умоўных графiчных скарачэнняў i iншых знакаў
%
% Based on rules approved by the law No 420-3 dated 23 July 2008
% About Belarusian orthography and punctuation
%
\patterns{"""

footer = "}"

def main():
    print(header)

    print("""%
% З аднаго радка на другi слова пераносiцца па складах.
% Words are hyphenated by syllables.
%
% во-ля, тра-ва, за-яц, га-ла-ва, ка-ва-лак,
% стра-ка-ты, пра-ве-рыць, пе-ра-кi-нуць.
%""")
    for v in V:
        print("{}1".format(v))

    print("""%
%   2. Калi ў сярэдзiне слова памiж галоснымi маецца спалучэнне зычных, то
% пераносiцца на наступны радок або ўсё гэта спалучэнне, або любая яго частка.
% If there are several consonants between vowels, all of them may be hyphenated
% or any part of it as well.
%
% ся-стра, сяс-тра, сяст-ра
% во-стры, вос-тры, вост-ры
% пту-шка, птуш-ка
% кро-пля, кроп-ля
% ма-ста-цтва, мас-тац-тва, мас-тацт-ва;
% ра-змова, раз-мова
% за-става, зас-тава
% ра-скрыць, рас-крыць, раск-рыць
% бя-скрыўдна, бяс-крыўдна, бяск-рыўдна
% дзя-цi-нства, дзя-цiн-ства, дзя-цiнс-тва, дзя-цiнст-ва
% двац-цаць, два-ццаць
% калос-се, кало-ссе
% сол-лю, со-ллю
% памяц-цю, памя-ццю
% мыц-ца, мы-цца
% паа-бапал, па-абапал
% насен-не, насе-нне
%""")
    for (c1, c2) in product(C, repeat=2):
        if c1 == "д" and c2 in "жз":
            print("% {}{} % special case".format(c1, c2))
        elif c1 == c2:
            # Prefer double consonants
            print("{}5{}".format(c1, c2))
        else:
            print("{}3{}".format(c1, c2))

    print("""%
% Пры пераносе нельга пакiдаць або пераносiць на наступны радок адну лiтару,
% нават калi яна адпавядае складу.
% A single letter can't be left of hyphenated, even if it forms a syllable.
%
% аса-ка, лi-нiя, ра-дыё, еха-лi, па-коi
%""")
    for v in V:
        print(".{}8".format(v))
        print("8{}.".format(v))

    print("""%
% Пры пераносе нельга разбiваць пераносам спалучэннi лiтар дж i дз,
% калi яны абазначаюць адзiн гук [дж], [дз’]:
% Combinations дж and дз shouldn't be split if they form a single sound.
%
% ура-джай, са-джаць, ра-дзi-ма, ха-дзiць
%
% Спалучэннi дж i дз можна разбiваць пераносам, калi д адносiцца да прыстаўкi,
% а з, ж – да кораня:
% These combinations can be split if д belongs to a prefix
% and ж or з to the root of a word.
%
% пад-жары, ад-жаць, пад-земны, ад-значыць
%""")
    for c in "жз":
        print("д2{}".format(c))

    print("""\
% Пры пераносе нельга аддзяляць ад папярэдняй галоснай лiтары й i ў.
% й and ў should not be separated from a preceding vowel.
%
% сой-ка, бой-кi, май-стар, дай-сцi, зай-мацца, праў-да, слоў-нiк, маў-чаць,
% заў-тра, праў-нук
%
% ** й ды ў ужываюцца выключна пасля галосных,
% таму можна забарону пераносу зрабіть агульнай для усіх літар.
% ** since й and ў can appear only after a vowel
% we can use a more general rule.
%""")
    for k in K:
        print("6{}1".format(k))

    print("""\
% Пры пераносе нельга  аддзяляць мяккi знак i апостраф ад папярэдняй зычнай.
% ь and ' should not be separated from a preceding consonant.
%
% буль-ба, прось-ба, вазь-му, бур’-ян, сем’-яў, мыш’-як
%
% ** Зычная з мяккім знакам ці апострафам з'яўляюцца часткай папярэдняга складу.
% ** A consonant and following ь or ' are part of a previous syllable.
%""")
    for s in A + M:
        for c in C:
            if (s in M) and (c in HC):
                # немагчымае спалучэнне
                # impossible combination
                print("% {}{} % impossible".format(c, s))
            else:
                print("6{}{}1".format(c, s))

    print("""%
% Зычныя літары не утвараюць склад, таму не пераносяцца,
% калі стаяць у пачатку ці канцы слова.
% Since consonants do not form syllables, it is not allowed to separate
% consonants in the beginning or ending of a word.
%""")
    for c in C + K:
        print(".{}8".format(c))
        print("8{}.".format(c))
    for (c1, c2) in product(C, C + M + A):
        if ((c1 in HC) and (c2 in M)):
            # Skip hard-only consonants followed by a soft sign
            print("% {}{}".format(c1, c2))
        else:
            print(".{}{}8".format(c1, c2))
            if c2 in A:
                # Quote can't be the last symbol in a word
                print("% {}{}.".format(c1, c2))
            else:
                print("8{}{}.".format(c1, c2))
    for (c1, c2, c3) in product(C, C + M, C + M + A):
        if ((c1 in HC) and (c2 in M)) or ((c2 in HC) and (c3 in M)) \
           or ((c2 in M) and (c3 in (M + A))):
            # Skip hard-only consonants followed by a soft sign
            # or combinations with ьь or ь'
            print("% {}{}{}".format(c1, c2, c3))
        else:
            print(".{}{}{}8".format(c1, c2, c3))
            if c3 in A:
                # Quote can't be the last symbol in a word
                print("% {}{}{}.".format(c1, c2, c3))
            else:
                print("8{}{}{}.".format(c1, c2, c3))

    print("""%
% Стылістычна лепш не аддзяляць прыстаўку не- ад слова. Інакш, гэта можа
% паўплываць на разуменне тексту.
%
% It is better not to separate prefix не- from a word.
% Alternatively this can affect understanding.
%
.не8
.ня8""")

    print("""%
% Перанос пасля некаторых прыставак толькі для слоў пачынаючыхся з зычных.
% Калі пасля ідзе галосная, вельмі верагодна што гэта не прыстаўка,
% а частка кораня.
%
% Hyphenation after several prefixes only for following consonants.
% If following letter is a vowel, it's very likely that the prefix
% is actually a part of the root.
%""")
    for p in ["ад", "над", "пад", "перад", "аб", "раз", "уз", "ўз",
              "праз", "ус", "ўс", "рас", "роз", "бяз", "без", "бяс",
              "бес", "рос", "цераз", "церас"]:
        print("% {}-".format(p))
        if len(p) > 2:
            # Assuming we have prefix in form of (cv)+c
            p = p[:-1] + '2' + p[-1:]
        for c in C:
            print(".{}3{}6".format(p, c))

    print(
"""% Перанос у словах, якія ўяўляюць сабой
% выключэнні з вышэй  апісаных правілаў
.ад8зін
тэ8мбр.
.дву8х3
.тро8х3
.чатыро8х3
слова7ў8твар
віда1з8мян
віда1з8мен
за1п8люшч
.па5д8зял
.па5д8зел
вё8рст
раз5г8ляд
раз5г8лед
зло1ў8жыв
.па5д8зяк
.вы1к8люч
.шма8т1
крова3ў8твар
за3ц8вярдз
.па3г8лядз
на5д8вор""")

    print(footer)
    print()

if __name__ == "__main__":
    main()
