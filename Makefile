.PHONY: all clean modules deb test-doc test-doc-clean

all: test-hyph-be.fmt

%.fmt: %.tex
		xetex -halt-on-error -file-line-error -ini -etex $<

clean: test-doc-clean
		rm -f *.aux *.pdf *.log *~ *.fmt

test-hyph-be.fmt: hyph-be.tex

hyph-be.tex: hyph-be.py
		./$< > $@

modules:
		git submodule init
		git submodule update

deb: texlive-hyph-belarusian_2014.20141024-1_all.deb

texlive-hyph-belarusian_2014.20141024-1_all.deb: hyph-be.tex
		./build-deb.sh

test-doc:
		make -C test-doc

test-doc-clean:
		make -C test-doc clean
