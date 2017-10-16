# SingleYarn.py

#Create an object of the CTextile class 
textile = CTextile( )

#Create a single yarn object:
yarn = CYarn( )

#Add 3 nodes to the yarn, specifying the coordinate positions only:
yarn.AddNode( CNode( XYZ(0, 0.0, 0)) )
yarn.AddNode( CNode( XYZ(1, 3.5, 0)) )
yarn.AddNode( CNode( XYZ(0, 7.0, 0)) )

# Add repeat vectors
yarn.AddRepeat( XYZ(3, 0, 0) )
yarn.AddRepeat( XYZ(0, 7, 0) )
yarn.AddRepeat( XYZ(0.5, 0, 1) )

# Add the yarn to the textile 
textile.AddYarn( yarn )	

Plower = XYZ(-0.5, 0, -0.5)
Pupper = XYZ(5*1.5, 5*7, 5*0.5)
textile.AssignDomain( CDomainPlanes(Plower, Pupper) )


# Add the textile with the name "single yarn" to the TexGen database
# If the script is run from within the TexGen GUI the yarn is displayed
AddTextile("single yarn", textile)
