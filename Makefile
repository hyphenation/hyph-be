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

.PHONY: all dist-clean modules

all: hyph-be.tex dz.txt

dist-clean:
		rm -f hyph-be.tex 3-letter-rules.txt dz.txt

hyph-be.tex: hyph-be.py 3-letter-rules.txt dz.py
		./hyph-be.py > $@

dz.txt: dz.py word-list.txt
		./dz.py word-list.txt > $@

3-letter-rules.txt: 3-letter-rules.py word-list.txt
		./$< word-list.txt >$@

word-list.txt: /usr/share/hunspell/be_BY.dic /usr/share/hunspell/be_BY.aff
		unmunch $^ >$@ 2>/dev/null

modules:
		git submodule init
		git submodule update
