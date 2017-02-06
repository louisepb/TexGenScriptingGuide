#Create a textile and  yarn
textile = CTextile()
yarn = CYarn() 

#Add nodes to the yarn
yarn.AddNode( CNode( XYZ(0.25, 5, 0.1), XYZ(0,-1,0),  XYZ(0, 0, 1) ) )
yarn.AddNode( CNode( XYZ(0.00, 1,  0),   XYZ(0,-1,0),  XYZ(0, 0, 1) ) )

# Set up a vector of points to specify the 2D yarn cross-section
Points = XYVector()

Points.push_back(XY(1.47887, -0.080294))
Points.push_back(XY( 1.1267, 0.0421169))
Points.push_back(XY( 0.763247, 0.123317))
Points.push_back(XY( 0.393884, 0.173093))
Points.push_back(XY( 0.0221259, 0.190496))
Points.push_back(XY( -0.349862, 0.166824))
Points.push_back(XY(-0.716936, 0.103844))
Points.push_back(XY( -1.26423, -0.0106595))
Points.push_back(XY( -0.94015, -0.143083))
Points.push_back(XY(-0.567315, -0.141597))
Points.push_back(XY( 0.178121, -0.132177))
Points.push_back(XY( 0.550909, -0.13775))
Points.push_back(XY( 0.923697, -0.14277))
Points.push_back(XY( 1.10991, -0.133933))

# Create polygon section with point vector
Shape = CSectionPolygon(Points)
ScaledShape = CSectionScaled( Shape, XY(2,1))

# Specify constant cross-section
Section = CYarnSectionConstant( ScaledShape )

# Assign cross-section to yarn
yarn.AssignSection( Section )

# Add yarn to textile
textile.AddYarn( yarn )           
AddTextile( "demo", textile )  
