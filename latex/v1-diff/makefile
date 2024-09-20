# begin of configurable section
LATEX = pdflatex
LATEX_OPTIONS = -shell-escape -halt-on-error
# end of configurable section

CLEANFILES_MAIN = *.ps *.log *.bak *.blg *.dvi *.toc *.out *.nav *.snm *.vrb *.listing
CLEANFILES = $(CLEANFILES_MAIN) *.aux

all: main_v0.pdf main_v1.pdf main_diff.pdf clean_main

main_v0.pdf: main_v0.tex main_v0.bbl
	outfile=`mktemp .tex.XXXXXX`; \
	echo 'Rerun' > $$outfile; \
	until ! grep 'Rerun' $$outfile; do \
		$(LATEX) $(LATEX_OPTIONS) $< | tee $$outfile; \
	done; \
	$(RM) $$outfile

main_v0.bbl: references_v0.bib
	$(LATEX) $(LATEX_OPTIONS) main_v0.tex
	bibtex main_v0

main_v1.pdf: main_v1.tex main_v1.bbl
	outfile=`mktemp .tex.XXXXXX`; \
	echo 'Rerun' > $$outfile; \
	until ! grep 'Rerun' $$outfile; do \
		$(LATEX) $(LATEX_OPTIONS) $< | tee $$outfile; \
	done; \
	$(RM) $$outfile

main_v1.bbl: references_v1.bib
	$(LATEX) $(LATEX_OPTIONS) main_v1.tex
	bibtex main_v1

main_diff.pdf: main_diff.tex main_diff.bbl
	outfile=`mktemp .tex.XXXXXX`; \
	echo 'Rerun' > $$outfile; \
	until ! grep 'Rerun' $$outfile; do \
		$(LATEX) $(LATEX_OPTIONS) $< | tee $$outfile; \
	done; \
	$(RM) $$outfile

main_diff.tex: main_v0.tex references_v0.bib main_v1.tex references_v1.bib
	latexdiff main_v0.tex main_v1.tex > main_diff.tex

main_diff.bbl: main_v0.bbl main_v1.bbl
	latexdiff main_v0.bbl main_v1.bbl > main_diff.bbl

.PHONY: clean clean_main distclean

clean:
	$(RM) $(CLEANFILES)

clean_main:
	$(RM) $(CLEANFILES_MAIN)

distclean: clean
	$(RM) main_v0.bbl main_v1.bbl main_diff.bbl
	$(RM) main_v0.pdf main_v1.pdf main_diff.pdf
	$(RM) -r _minted-main
