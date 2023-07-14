# DecoupledLToLTextile.py

# Python 3 version used runpy module to execute scripts from TexGen GUI which requires import of library
from TexGen.Core import *

#Set up 3D Weave textile
numBinderLayers = 2
numXYarns = 4
numWefts = 6

warpSpacing = 1.42
weftSpacing = 1.66
warpHeight = 0.3
weftHeight = 0.3

Textile = CTextileDecoupledLToL( numXYarns, numWefts, warpSpacing, weftSpacing, warpHeight, weftHeight, numBinderLayers, True)

#set number of binder / warp yarns
NumBinderYarns = 2

BinderRatio = 1
WarpRatio = 1
Textile.SetWarpRatio( WarpRatio )
Textile.SetBinderRatio( BinderRatio )

# Set up layers: 2 warp, 3 weft
Textile.SetupLayers( 2, 3, numBinderLayers)

# Define offsets for the two binder yarns
binderYarns = [[[0, 1, 1, 2, 1, 0], 
                [3, 2, 3, 3, 2, 3]],
               [[1, 0, 1, 0, 2, 1],
               [2, 3, 2, 2, 3, 2]]]

#Check if length of binderYarns positions equal to numWefts
for z in range(NumBinderYarns):
    for y in range( numBinderLayers ):
        if len(binderYarns[z][y]) != numWefts:
            raise Exception("Too many binder yarn positions specified, must be equal to number of wefts.")

binderWidth = 1.2
binderHeight = 0.3
warpWidth = 1.2
weftWidth = 1.2

Textile.SetYYarnWidths( weftWidth )
Textile.SetXYarnWidths( warpWidth )
Textile.SetBinderYarnWidths( binderWidth )
Textile.SetBinderYarnHeights( binderHeight )
Textile.SetBinderYarnPower( 0.2 )
Textile.SetWarpYarnPower(1.0)
Textile.SetWeftYarnPower(1.0)
        
#Decompose binder yarn offsets into stacks

repeat = BinderRatio + WarpRatio

# Loop for the number of binder yarn stacks
for z in range(NumBinderYarns):
    # Loop through the weft stacks
    for x in range( numWefts ):
        zOffsets = IntVector()
        
        # Loop through binder layers
        for y in range( numBinderLayers):
            zOffsets.push_back(int(binderYarns[z][y][x]))
            
        # Calculate the binder y position (ie warp yarn index)
        ind = z/BinderRatio
        BinderIndex = WarpRatio + (ind * repeat) + z%BinderRatio
        Textile.SetBinderPosition(x, int(BinderIndex), zOffsets)

Textile.SetWeftRepeat( True )
Textile.AssignDefaultDomain( )

Textile.SetFibresPerYarn(WARP, 12000)
Textile.SetFibresPerYarn(WEFT, 12000)
Textile.SetFibresPerYarn(BINDER, 12000)
Textile.SetFibreDiameter(WARP, 0.0026, "mm")
Textile.SetFibreDiameter(WEFT, 0.0026, "mm")
Textile.SetFibreDiameter(BINDER, 0.0026, "mm")

Textile.BuildTextile()
AddTextile( Textile )
	
	



	
