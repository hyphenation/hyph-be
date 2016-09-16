.PHONY: all

all: document.t2a.pdf document.pdf

document.t2a.pdf: document.t2a.tex
		pdflatex $<

document.pdf: document.tex
		xelatex $<
