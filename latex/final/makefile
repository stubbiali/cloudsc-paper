# begin of configurable section
LATEX = pdflatex
LATEX_OPTIONS = -shell-escape -halt-on-error
# end of configurable section

CLEANFILES_MAIN = *.ps *.log *.bak *.blg *.dvi *.toc *.out *.nav *.snm *.vrb *.listing
CLEANFILES = $(CLEANFILES_MAIN) *.aux

all: main.pdf clean_main

main.pdf: main.tex main.bbl
	outfile=`mktemp .tex.XXXXXX`; \
	echo 'Rerun' > $$outfile; \
	until ! grep 'Rerun' $$outfile; do \
		$(LATEX) $(LATEX_OPTIONS) $< | tee $$outfile; \
	done; \
	$(RM) $$outfile

main.bbl: references.bib
	$(LATEX) $(LATEX_OPTIONS) main.tex
	bibtex main

.PHONY: clean clean_main distclean

clean:
	$(RM) $(CLEANFILES)

clean_main:
	$(RM) $(CLEANFILES_MAIN)

distclean: clean
	$(RM) main.bbl main.pdf
	$(RM) -r _minted-main
