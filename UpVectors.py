#Create a textile and  yarn
textile = CTextile()
yarn = CYarn() 

#Add nodes to the yarn
# First parameter is node position
# Second parameter is tangent at node
# Third parameter is Up vector of node
# Using default 2nd and 3rd parameters results in twisting of yarn
yarn.AddNode( CNode( XYZ(0.25, 5, 0.1), XYZ(0,-1,0),  XYZ(0, 0, 1) ) )
yarn.AddNode( CNode( XYZ(0.50, 3,  0),   XYZ(0,-1,0),  XYZ(0, 0, 1) ) )
yarn.AddNode( CNode( XYZ(0.00, 1,  0),   XYZ(0,-1,0),  XYZ(0, 0, 1) ) )
yarn.AddNode( CNode( XYZ(0.00, 1, -5),   XYZ(0,0,-1),  XYZ(0,-1,0) ) ) 

# Add nodes to the yarn
textile.AddYarn( yarn )     
# Add the textile to the TexGen database     
AddTextile( "demo", textile )  
