# Python 3 version used runpy module to execute scripts from TexGen GUI which requires import of library
from TexGen.Core import *

# Create an orthogonal textile with 6 warp and 4 weft yarns, 1.0 warp and weft spacing, 
# warp height 0.35 and weft height 0.25. True/False selects refinement
Textile = CTextileOrthogonal( 6, 4, 1.0, 1.0, 0.35, 0.25, True)

# Set the ratio of warp/binder yarns
Textile.SetWarpRatio( 2 )
Textile.SetBinderRatio( 1 )

# Add yarn layers. 
# Set up numbers of warp and weft layers
NumWarpLayers = 2
NumWeftLayers = 3
Textile.SetupLayers( NumWarpLayers, NumWeftLayers )

# Alternatively the layers can be added manually if a different configuration 
# to the standard alternating warp and weft layers is required.  There must 
# always be one NoYarn layer and one Binder layer
#Textile.AddNoYarnLayer()
#Textile.AddYLayers()
#Textile.AddWarpLayer()
#Textile.AddYLayers()
#Textile.AddWarpLayer()
#Textile.AddYLayers()
#Textile.AddBinderLayer()



# Adjust the yarn widths, heights and spacings
Textile.SetWarpYarnWidths( 3.6 )
Textile.SetWarpYarnHeights( 0.35 )
Textile.SetWarpYarnSpacings( 3.8 )

Textile.SetBinderYarnWidths( 1.375 )
Textile.SetBinderYarnHeights( 0.16 )
Textile.SetBinderYarnSpacings( 1.4 )

# Weft yarns
Textile.SetYYarnWidths(2.58)  
Textile.SetYYarnSpacings(2.8)

# Set the power of the power ellipses used
Textile.SetWarpYarnPower(0.6)
Textile.SetWeftYarnPower(0.6)
Textile.SetBinderYarnPower(0.8)

# Binder yarns may only be at top/bottom position in orthogonal
# In this case the binder layer was created as the top layer so switching will place them at the bottom
Textile.SwapBinderPosition( 0,2)
Textile.SwapBinderPosition( 2,2)
Textile.SwapBinderPosition( 1,5)
Textile.SwapBinderPosition( 3,5)

# Create a default domain to fit the textile
Textile.AssignDefaultDomain()

# Set fibre properties
Textile.SetFibreDiameter( WARP, 0.007, "mm" )
Textile.SetFibreDiameter( WEFT, 0.007, "mm" )
Textile.SetFibreDiameter( BINDER, 0.007, "mm" )
Textile.SetFibresPerYarn( WARP, 5000 )
Textile.SetFibresPerYarn( WEFT, 8000 )
Textile.SetFibresPerYarn( BINDER, 3500 )
# Set the target thickness for the refined textile
Textile.SetThickness(1.4)
# Set the maximum volume fraction allowed in the refine process
Textile.SetMaxVolFraction(0.78)
# Reset the domain height to suit the refined textile
Textile.SetDomainZValues()

# Add the textile
AddTextile(Textile)