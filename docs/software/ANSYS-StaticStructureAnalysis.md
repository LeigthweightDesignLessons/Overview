# ACP (PRE)

| Toolbox  | Name  |
|:--- | :--- |
| Komponentensysteme | Geometrie |


## Gruppen

Ändert sich die Geometrie ändern sich normalerweise auch die Zuweisungen.
Dies hat zur folge, dass bestimmte Zuweisungen in anderen Simulationen nicht mehr funktionieren.
Um dies zu verhindern kann man Gruppen zu weisen!




## Scripting

Das Scripting mit Python erlaubt in SpaceClaim Prozesse, 
wie die Geometrieerstellung und -bearbeitung zu automatisieren.

Ein neues Skript kann unter:<br>
Datei/Neu/Skript<br>
erstellt werden.

Mit Hilfe der **Aufzeichnen**-Funktion werden direkte Handlungen in Programmcode übersetzt.


??? info "Beispiel: Kugel auf Platte"
    Mit dem folgenden Code lässt sich folgende Geometrie automatisch erzeugen und anpassen:
    ````python linenums="1"
    --8<-- "examples/sphere_impact/generate_geometry.py"
    ````

Weiter Informationen zu Thema Scripting in SpaceClaim findet man [hier](http://help.spaceclaim.com/2017.0.0/en/Content/Scripting.htm).

