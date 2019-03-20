# HybridSections.py

#Create an object of the CTextile class 
textile = CTextile( )

#Create a single yarn object:
yarn = CYarn( )

#Add 3 nodes to the yarn, specifying the coordinate positions only:
yarn.AddNode( CNode( XYZ(0, 0.0, 0)) )
yarn.AddNode( CNode( XYZ(1, 3.5, 0)) )
yarn.AddNode( CNode( XYZ(0, 7.0, 0)) )

sections = CYarnSectionInterpNode()

# Hybrid with two sections
Top = CSectionEllipse( 1.0, 0.4 )
Bottom = CSectionPowerEllipse( 1.0, 0.4, 0.4, 0.25 )
sections.AddSection( CSectionHybrid( Top, Bottom ) )

#Hybrid with four sections
TopLeft = CSectionRectangle(1.0, 0.4)
TopRight = CSectionEllipse( 1.0, 0.4 )
BottomLeft = CSectionPowerEllipse(1.0, 0.4, 1.5)
BottomRight = CSectionPowerEllipse( 1.0, 0.4, 0.4, 0.25 )
sections.AddSection( CSectionHybrid(TopRight, TopLeft, BottomLeft, BottomRight) )

# Hybrid specifying position of divisions
Hybrid = CSectionHybrid()
Hybrid.AddDivision(0.25)
Hybrid.AddDivision(0.75)
Hybrid.AssignSection(0, CSectionLenticular(1.0,0.4))
Hybrid.AssignSection(1, CSectionEllipse(1.0,0.4))
sections.AddSection(Hybrid)

# Assign sections to yarn
yarn.AssignSection( sections )

# Add the yarn to the textile 
textile.AddYarn( yarn )	

# Add the textile with the name "yarn sections hybrid" to the TexGen database
# If the script is run from within the TexGen GUI the yarn is displayed
AddTextile("yarn sections hybrid", textile)
