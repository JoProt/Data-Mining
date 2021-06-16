TARG = kap6_pres

# Für die Meta-Schrift brauchen wir eine spezielle
# LaTeX-Engine -> entweder xelatex oder lualatex
ENGINE = xelatex

all:	${TARG}.tex
	latexmk -${ENGINE} ${TARG}

clean:
	latexmk -${ENGINE} -c
	rm ${TARG}.snm ${TARG}.nav ${TARG}.xdv
