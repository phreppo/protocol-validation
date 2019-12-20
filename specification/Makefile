PROP_DIR ?= properties
PROPERTIES_SOURCES := $(shell find $(PROP_DIR) -name *.mcf)
PROPERTIES_COMPILED := $(PROPERTIES_SOURCES:%=%.pbes)

all: clean test
	@ rm -f *.lps *.lts
	@ rm -f $(PROP_DIR)/*.pbes
	@ python3 build.py

code_spec.lps:
	mcrl22lps code_spec.mcrl2 code_spec.lps --lin-method=regular2
code_spec.lts: code_spec.lps
	lps2lts code_spec.lps code_spec.lts
	@ echo "\e[32m✓\e[39m Specification parsing executed"

test: code_spec.lts $(PROPERTIES_COMPILED)
	@ echo "\e[32m✓\e[39m Properties tested"

$(PROP_DIR)/%.mcf.pbes: $(PROP_DIR)/%.mcf code_spec.lts
	@ echo -e '  \e[96mSolving\e[34m' $@ '\e[39m'
	@ lps2pbes --formula=$< code_spec.lps $@ -m
	@ pbessolve $@

parse: code_spec.lts
	@ rm -f *.lps *.lts
	@ rm -f $(PROP_DIR)/*.pbes

run: code_spec.lts
	lpssim code_spec.lps
	@ rm -f *.lps *.lts
	@ rm -f $(PROP_DIR)/*.pbes

clean:
	@ rm -f *.lps *.lts
	@ rm -f $(PROP_DIR)/*.pbes