.PHONY: all clean

all: document.t2a.pdf document.pdf

clean:
		-rm -f *.pdf *.aux *.log *~

document.t2a.pdf: document.t2a.tex
		pdflatex $<

document.pdf: document.tex
		xelatex $<
