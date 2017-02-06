# Create a 4x4 2d woven textile with yarn spacing of 5 and thickness 2
# The fourth parameter is the shear angle in radians
# The sixth parameter indicates whether to refine the textile to avoid intersections
Textile = CShearedTextileWeave2D(4, 4, 5, 2, 5*pi/180.0, True);

# Set the weave pattern
Textile.SwapPosition(3, 0);
Textile.SwapPosition(2, 1);
Textile.SwapPosition(1, 2);
Textile.SwapPosition(0, 3);

# Adjust the yarn width and height
Textile.SetYarnWidths(4);
Textile.SetYarnHeights(0.8);

# Setup a default domain
# Use True parameter to generate a sheared domain (otherwise the 
# domain will be aligned to the axes, cutting the yarns
Textile.AssignDefaultDomain( True )

# Add the textile
AddTextile(Textile)
