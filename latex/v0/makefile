# begin of configurable section
LATEX = pdflatex
LATEX_OPTIONS = -shell-escape -halt-on-error
MAIN_SRC = main.tex
SUBFILES_SRC = \
	subfiles/abstract.tex \
	subfiles/acknowledgements.tex \
	subfiles/preamble.tex \
	subfiles/section01.tex \
	subfiles/section02.tex \
	subfiles/section03.tex \
	subfiles/section04.tex \
	subfiles/section05.tex \
	subfiles/section06.tex \
	subfiles/title.tex
BIB_SRC = subfiles/references.bib
INC =
FIGS =
# end of configurable section

MAIN_TRG = $(MAIN_SRC:.tex=.pdf)
MAIN_BASE = $(basename $(MAIN_SRC))
SUBFILES_TRG = $(SUBFILES_SRC:.tex=.pdf)
BIB_TRG=$(MAIN_SRC:.tex=.bbl)
CLEANFILES_MAIN = *.ps *.log *.bak *.blg *.dvi *.toc *.out *.nav *.snm *.vrb *.listing
CLEANFILES = $(CLEANFILES_MAIN) *.aux

all: $(MAIN_TRG) clean_main

$(MAIN_TRG): $(MAIN_SRC) $(SUBFILES_SRC) $(BIB_TRG) $(FIGS) $(INC)
	outfile=`mktemp .tex.XXXXXX`; \
	echo 'Rerun' > $$outfile; \
	until ! grep 'Rerun' $$outfile; do \
		$(LATEX) $(LATEX_OPTIONS) $< | tee $$outfile; \
	done; \
	$(RM) $$outfile

$(SUBFILES_TRG): %.pdf: %.tex $(FIGS) $(INC)
	outfile=`mktemp .tex.XXXXXX`; \
	echo 'Rerun' > $$outfile; \
	until ! grep 'Rerun' $$outfile; do \
		$(LATEX) $(LATEX_OPTIONS) $< | tee $$outfile; \
	done; \
	$(RM) $$outfile

$(BIB_TRG): $(BIB_SRC) $(MAIN_SRC)
	$(LATEX) $(LATEX_OPTIONS) $(MAIN_SRC)
	bibtex $(MAIN_BASE)

.PHONY: clean clean_main distclean

clean:
	$(RM) $(CLEANFILES)

clean_main:
	$(RM) $(CLEANFILES_MAIN)

distclean: clean
	$(RM) $(SUBFILES_TRG)
	$(RM) $(BIB_TRG)
	$(RM) $(MAIN_TRG)
	$(RM) -r _minted-main

img:
	for script in $(PYTHON_SCRIPTS) ; do \
        python $$script --no-show --save ; \
    done
