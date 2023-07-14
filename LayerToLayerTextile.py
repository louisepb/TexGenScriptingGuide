# Python 3 version used runpy module to execute scripts from TexGen GUI which requires import of library
from TexGen.Core import *

#create textile
NumBinderLayers = 2 
NumXYarns = 3 
NumYYarns = 4 
XSpacing = 1.0
YSpacing = 1.0 
XHeight = 0.2 
YHeight = 0.2 

weave = CTextileLayerToLayer(NumXYarns, NumYYarns, XSpacing,
           YSpacing, XHeight, YHeight, NumBinderLayers)

#set number of binder / warp yarns
NumBinderYarns = 2
NumWarpYarns = NumXYarns - NumBinderYarns
weave.SetWarpRatio( NumWarpYarns )
weave.SetBinderRatio( NumBinderYarns )

#setup layers: 3 warp, 4 weft
weave.SetupLayers( 3, 4, NumBinderLayers)

#set yarn dimensions: widths / heights
weave.SetYYarnWidths( 0.8 )
weave.SetYYarnWidths( 0.8 )
weave.SetBinderYarnWidths( 0.4 )
weave.SetBinderYarnHeights( 0.1 )

#define offsets for the two binder yarns
P = [[0, 1, 3, 0],[3, 0, 0, 3]]

#assign the z-positions to the binder yarns
for y in range(NumWarpYarns,NumXYarns): #loop through number of binder yarns
	offset = 0 
	for x in range(0,NumYYarns): #loop through the node positions	
		weave.SetBinderPosition(x, y, P[y-NumWarpYarns][offset])
		offset = offset+1
		
# Add textile to database
AddTextile('test3D', weave)
