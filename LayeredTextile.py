#Create a plain weave textile
t = 0.1 #layer thickness
weave = CTextileWeave2D( 2, 2, 0.8, t, True )
weave.SwapPosition(0, 0) 
weave.SwapPosition(1, 1)
weave.SetGapSize(0.01) # set a gap between yarns

#Create the layered textile
LTextile = CTextileLayered()

# Add a plain weave layer with no offsets
LTextile.AddLayer( weave, XYZ(0, 0, 0) )

# Add a second plain weave layer, offset in the z-direction
# by the textile thickness and by 0.5 and 0.5 in the x and y directions
LTextile.AddLayer( weave, XYZ(0.5, 0.5, t) )

# Get the default domain of the plain weave and its min and max coordinates
Domain = weave.GetDefaultDomain()
Min = XYZ()
Max = XYZ()
Domain.GetBoxLimits( Min, Max )

# Get the domain upper surface
Plane = PLANE()
index = Domain.GetPlane( XYZ(0,0,-1), Plane )
# Offset the top surface of the domain by the depth of the plain weave domain
Plane.d -= Max.z - Min.z
Domain.SetPlane( index, Plane )

# Assign the extended domain to the layered textile
LTextile.AssignDomain( Domain )

#Add the textile to the database
AddTextile( "LayeredTex", LTextile )

