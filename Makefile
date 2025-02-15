MAIN=cv

all: $(MAIN).pdf

$(MAIN).pdf: $(MAIN).tex
	pdflatex -interaction=batchmode $^

$(MAIN).tex: data.toml
	python write_curriculum.py > $@

clean:
	rm -rf $(MAIN).pdf $(MAIN).tex *.aux *.log *.out

.PHONY: all clean
