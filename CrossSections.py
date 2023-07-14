# CrossSections.py

# Python 3 version used runpy module to execute scripts from TexGen GUI which requires import of library
from TexGen.Core import *
from math import *

# Create textile
textile = CTextile( )

# Create yarn
yarn = CYarn( )

# Add nodes to yarn
yarn.AddNode( CNode(XYZ(0, 0.0, 0)) )
yarn.AddNode( CNode(XYZ(1, 3.5, 0)) )
yarn.AddNode( CNode(XYZ(0, 7.0, 0)) )

#Define three different cross-sectional shapes at the master nodes 
section=CYarnSectionInterpNode()
section.AddSection(CSectionEllipse(1, 0.1))
section.AddSection(CSectionRotated(CSectionEllipse(1, 0.1), radians(45)) )
section.AddSection(CSectionPowerEllipse (2, 0.3, 0.1, 0.0))

#Assign the cross-sections to the yarn and add to the textile 
yarn.AssignSection(section)
textile.AddYarn(yarn)	

#Add the textile to the database
AddTextile("varying shapes", textile)
