# LS-DYNA

### Installation

Da LS-DYNA von ANSYS gekauft wurde bieten sich dem Nutzer zwei Möglichkeiten:

1. Benutzung der **Standalone**-Produkte, 
    die vollen Funktionsumfang bieten sich jedoch nur schwer in den ANSYS Workflow mit einbinden lassen.
2. Benutzung der **ANSYS-Workbench-Erweiterung**, 
    welche zwar in ihrem Funktionsumfang limitiert ist, 
    sich dafür aber sehr leicht in einen bestehenden Workflow einbinden lässt.

#### Standalone

=== "Windows"
    1. Herunterladen von LS-DYNA ([Link](https://files.dynamore.de/dyna-versions/LSTC-Winsuite/LSTC-WinSuite_R12.0_r114-win-x64-installer.exe ))
    1. Installation durch Ausführen der EXE
    1. Einrichten der Lizenzservers
        1. Starte LS-RUN
          <figure>
            <img src="../../img/software/ls_dyna-win-ls-run.png" width="150" />
            <figcaption>In der Suchleiste ``LS-Run`` eingeben und entsprechendes Programm auswählen.</figcaption>
          </figure>
        1. Auswahl der Lizens
          <figure>
            <img src="../../img/software/ls_dyna-win-license.png" width="500" />
            <figcaption>Auswahl der Lizens unter ``License->LS-DYNA License``</figcaption>
          </figure>
        1. Einrichten des Lizensservers
          <figure>
            <img src="../../img/software/ls_dyna-win-netzwerk.png" width="500" />
            <figcaption>Bei **License type:** ``Network`` und bei **Server hostname:** ``lsdyna.htwk-leipzig.de`` eingeben. Überprüfen ob bei **License Info** die entsprechenden Informationen angezeigt werden.</figcaption>
          </figure>

=== "Linux"

#### ANSYS-Workbench Erweiterung

???+ warning "Achtung"
    Die folgenden Schritte müssen für jedes neue Projekt wiederholt werden!

1. Öffnen der Workbench
2. Öffne **Erweiterungen**
3. Klicke **Verwalte Erweiterungen...**
4. Aktiviere **LSDYNA**

<figure>
  <img src="../../img/software/ls_dyna-ansys.png" width="600" />
</figure>

### Lernmaterialien

- Einführung in die LS-DYNA PrePost Oberfläche [Video](https://www.youtube.com/watch?v=uFhkB_pvU8k)
- Material-Modelierung [Video](https://www.youtube.com/watch?v=z46He6FivSU)
