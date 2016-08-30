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
\message{Loading hyphenation patterns for Belarusian}
\patterns{"""

footer = "}"

def main():
    print(header)

    print("""\
%   1. З аднаго радка на другi слова пераносiцца па складах:
% во-ля, тра-ва, за-яц, га-ла-ва, ка-ва-лак,
% стра-ка-ты, пра-ве-рыць, пе-ра-кi-нуць.""")
    for v in V:
        print("{}1".format(v))

    print("""\
%   2. Калi ў сярэдзiне слова памiж галоснымi маецца спалучэнне зычных, то
% пераносiцца на наступны радок або ўсё гэта спалучэнне, або любая яго частка. Можна
% пераносiць: ся-стра, сяс-тра, сяст-ра; во-стры, вос-тры, вост-ры; пту-шка, птуш-ка;
% кро-пля, кроп-ля; ма-ста-цтва, мас-тац-тва, мас-тацт-ва; ра-змова, раз-мова;
% за-става, зас-тава; ра-скрыць, рас-крыць, раск-рыць; бя-скрыўдна, бяс-крыўдна,
% бяск-рыўдна; дзя-цi-нства, дзя-цiн-ства, дзя-цiнс-тва, дзя-цiнст-ва; двац-цаць,
% два-ццаць; калос-се, кало-ссе; сол-лю, со-ллю; памяц-цю, памя-ццю; мыц-ца, мы-цца;
% паа-бапал, па-абапал; насен-не, насе-нне.""")
    for (c1, c2) in product(C, repeat=2):
        if c1 == "д" and c2 in "жз":
            print("% {}{} % special case".format(c1, c2))
        elif c1 == c2:
            # Prefer double consonants
            print("{}5{}".format(c1, c2))
        else:
            print("{}3{}".format(c1, c2))

    print("""\
% 3. Пры пераносе нельга:
%   пакiдаць або пераносiць на наступны радок адну лiтару, нават калi яна адпавядае
% складу: аса-ка, лi-нiя, ра-дыё, еха-лi, па-коi;""")
    for v in V:
        print(".{}8".format(v))
        print("8{}.".format(v))

    print("""\
%   разбiваць пераносам спалучэннi лiтар дж i дз, калi яны абазначаюць адзiн гук
% [дж], [дз’]: ура-джай, са-джаць, ра-дзi-ма, ха-дзiць. Спалучэннi дж i дз можна
% разбiваць пераносам, калi д адносiцца да прыстаўкi, а з, ж – да кораня: пад-жары,
% ад-жаць, пад-земны, ад-значыць;""")
    for c in "жз":
        print("д2{}".format(c))

    print("""\
%   аддзяляць ад папярэдняй галоснай лiтары й i ў: сой-ка, бой-кi, май-стар, дай-сцi,
% зай-мацца, праў-да, слоў-нiк, маў-чаць, заў-тра, праў-нук;
%   аддзяляць мяккi знак i апостраф ад папярэдняй зычнай: буль-ба, прось-ба,
% вазь-му, бур’-ян, сем’-яў, мыш’-як.""")
    for c in M + K + A:
        print("8{}1".format(c))

    print("""\
%   Зычныя літары не утвараюць склад, таму не пераносяцца,
% калі стаяць у пачатку ці канцы слова.""")
    for c in C + K + A:
        print(".{}8".format(c))
        print("8{}.".format(c))
    for (c1, c2) in product(C + A, repeat=2):
        print(".{}{}8".format(c1, c2))
        print("8{}{}.".format(c1, c2))

    print("% Лепш не аддзяляць прыстаўку не- ад слова")
    print(".не8")
    print(".ня8")

    for prefix in ["ад", "над", "пад", "перад", "аб", "раз", "уз", "праз", "ус", "рас", "роз", "бяз", "без", "бяс", "бес", "рос", "цераз", "церас"]:
        print("% Перанос пасля прыстаўкі {}-".format(prefix))
        for c in C:
            print(".{}3{}".format(prefix, c))

    print(
"""% Перанос у словах, якія ўяўляюць сабой
% выключэнні з вышэй  апісаных правілаў
.ад8зін
тэ8мбр.
8льш.
8сць.
8дзь.
.дву8х3
слова1ў8твар
віда1з8мян
віда1з8мен
за1п8люшч
.па1д8зял
.па1д8зел
вё8рст
раз1г8ляд
раз1г8лед
зло1ў8жыв
.па1д8зяк
.вы1к8люч
.шма8т1
крова3ў8твар
за3ц8вярдз
.па3г8лядз
на1д8вор""")

    print(footer)
    print()

if __name__ == "__main__":
    main()
