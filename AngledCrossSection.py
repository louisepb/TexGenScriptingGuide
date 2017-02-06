###############################################
#Create a straight yarn with constant elliptical cross-section
textile = CTextile( )
yarn = CYarn( )
yarn.AddNode( CNode(XYZ(0, 0.0, 0)) )
yarn.AddNode( CNode(XYZ(0, 3.5, 0)) )
yarn.AddNode( CNode(XYZ(0, 7.0, 0)) )
ellipse=CSectionEllipse(1, 0.3)
section = CYarnSectionConstant(ellipse)
yarn.AssignSection(section)

###############################################
#rotate the cross-sections at mid node
index=1 
node = yarn.GetNode(index)
node.SetAngle(PI/4)
yarn.ReplaceNode(index, node)

###############################################
#visualise the textile
textile.AddYarn(yarn)	
AddTextile("tex", textile)

