all: test-hyph-be.pdf

%.pdf: %.tex
		xetex -halt-on-error -file-line-error -ini -etex $<

clean:
		rm -f *.aux *.pdf *.log *~ *.fmt

test-hyph-be.pdf: hyph-be.tex

hyph-be.tex: hyph-be.py
		./$< > $@
