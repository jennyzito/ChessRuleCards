.PHONY: main clean FORCE

TEXTMP=.textmp

main: ChessRuleCards.pdf ChessRuleCards.png

%.tex: %.tex.py
	python $< > $@

%.pdf: %.tex
	mkdir -p $(TEXTMP)
	latexmk -auxdir=$(TEXTMP) -outdir=$(TEXTMP) -pdflatex='lualatex -halt-on-error -file-line-error -interaction=errorstopmode' -pdf $<
	mv $(TEXTMP)/$@ .

%.png:	%.pdf
	pdftoppm -singlefile -png $< $*

clean:
	latexmk -pdf -C
