LaTeX Beamer Thema für die Hochschule Wismar
--------------------------------------------

Das "Wismar" Thema gestaltet alle Folien in Anthrazit
mit Farbakzenten der drei Fakultäten.

Zusätzlich können die Folien in genau einer der drei
Fakultätsfarben gestaltet werden. Dafür wird eines
der Farbthemen
- FIW (blau)
- FWW (grün)
- FG (orange)
mit dem Kommando \usecolortheme{...} eingebunden.

Weitere Hinweise finden Sie im beiliegenden Beispiel (beispiel.tex).

Es liegt außerdem ein Makefile bei, um die Folien
als PDF zu generieren. Für die Übersetzung wird
entweder die TeX-Engine "XeTeX" oder "LuaTeX" benötigt
(Vorlage verwendet das "Fontspec" Paket, das eine
dieser beiden TeX-Engines voraussetzt).

Sie können eigene Folien in diesem Verzeichnis erstellen,
oder die Style-Dateien (*.sty) und alle ihre Abhängigkeiten
(*.pdf, Meta.fontspec, font/) in das entsprechende
Quellverzeichnis Ihrer LaTeX-Distribution verschieben, um
somit auch außerhalb dieses Verzeichnisses arbeiten zu
können.

Fragen und Änderungswünsche bitte an:
juergen.cleve@hs.wismar.de
l.gillner@stud.hs-wismar.de
