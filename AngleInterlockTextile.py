# Setup angle interlock textile with 3 warp yarns, 6 weft
# x and y spacing 1.5 and 1.0 respectively
# x and y yarn heights both 0.1
Textile = CTextileAngleInterlock( 3, 6, 1.5, 1.0, 0.1, 0.1)

# Warp ratio set to 0 therefore all warp yarns are binders
Textile.SetWarpRatio( 0 )
Textile.SetBinderRatio( 1 )

# Setup layers: 2 warps, 3 wefts 
Textile.SetupLayers( 2, 3 )

# Set yarn sizes
Textile.SetWarpYarnWidths( 1.2 )
Textile.SetBinderYarnWidths( 0.5 )
Textile.SetBinderYarnHeights( 0.05 )
Textile.SetWarpYarnHeights( 0.2 )
Textile.SetWarpYarnSpacings( 1.4 )
Textile.SetBinderYarnSpacings( 0.6 )
Textile.SetYYarnSpacings(1.2)

# Set the x,y position where the binder is at the top of the stack
Textile.SetBinderYarnPositions(2,2)
Textile.SetBinderYarnPositions(4,1)
Textile.SetBinderYarnPositions(0,0)

Textile.AssignDefaultDomain()

AddTextile(Textile)

