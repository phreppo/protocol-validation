COMPILE_CMD ?= pdflatex -jobname=report -quiet -interaction=nonstopmode main.tex > /dev/null 2>&1

all: report clean
	@ echo "\e[32m✓\e[39m Pdf report produced correctly"

report:
	@ $(COMPILE_CMD)
	@ $(COMPILE_CMD)
	@ $(COMPILE_CMD)
	@ $(COMPILE_CMD)

clean:
	@ rm -f *.synctex.gz *.fdb_latexmk *.fls *.aux *.log *.toc