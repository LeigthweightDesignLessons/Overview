# Python Script, API Version = V17

# Clear UP
selection = Selection.SelectAll()
Delete.Execute(selection)

width = Parameters.width
length = Parameters.length
thickness = Parameters.thickness
radius = Parameters.radius

# Set Sketch Plane
sectionPlane = Plane.Create(Frame.Create(Point.Create(MM(0), MM(0), MM(0)),
    Direction.DirX,
    Direction.DirY))
result = ViewHelper.SetSketchPlane(sectionPlane, Info1)
# EndBlock

# Sketch Rectangle
point1 = Point2D.Create(MM(-width/2),MM(length/2))
point2 = Point2D.Create(MM(width/2),MM(length/2))
point3 = Point2D.Create(MM(-width/2),MM(-length/2))
result = SketchRectangle.Create(point1, point2, point3)
# EndBlock

# Solidify Sketch
mode = InteractionMode.Solid
result = ViewHelper.SetViewMode(mode, Info4)
# EndBlock

# 1 Fläche strecken
selection = Selection.Create(Face2)
options = ExtrudeFaceOptions()
options.ExtrudeType = ExtrudeType.Add
result = ExtrudeFaces.Execute(selection, MM(thickness), options, Info5)
# EndBlock

# Kugel erstellen
SphereBody.Create(Point.Create(MM(0), MM(0), MM(radius + thickness)), Point.Create(MM(0), MM(0), MM(thickness)), ExtrudeType.Add, Info10)
# EndBlock

# "Volumenkörper" in "Plate" umbenennen
selection = Selection.Create(Body6)
result = RenameObject.Execute(selection,"Plate")
# EndBlock

# "Volumenkörper" in "Sphere" umbenennen
selection = Selection.Create(Body7)
result = RenameObject.Execute(selection,"Sphere")
# EndBlock

# Benannte Auswahlgruppe erstellen
primarySelection = Selection.Create(Face1, Face3, Face4, Face5)
secondarySelection = Selection()
result = NamedSelection.Create(primarySelection, secondarySelection)
# EndBlock

# Rename Named Selection
result = NamedSelection.Rename("Gruppe1", "Fixation_Face")
# EndBlock

# Benannte Auswahlgruppe erstellen
primarySelection = Selection.Create(Body1)
secondarySelection = Selection()
result = NamedSelection.Create(primarySelection, secondarySelection)
# EndBlock

# Benannte Auswahl umbenennen
result = NamedSelection.Rename("Gruppe1", "Plate")
# EndBlock

# Benannte Auswahlgruppe erstellen
primarySelection = Selection.Create(Body2)
secondarySelection = Selection()
result = NamedSelection.Create(primarySelection, secondarySelection)
# EndBlock

# Benannte Auswahl umbenennen
result = NamedSelection.Rename("Gruppe1", "Sphere")
# EndBlock
