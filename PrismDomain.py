# =============================================================================
# TexGen: Geometric textile modeller.
# Copyright (C) 2022 Louise Brown

# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
# =============================================================================

#Create a textile
textile = CTextile()

# Create vector for domain polygon points
points = XYVector()
 
# Add points to polygon and create prism domain using 
# the vector of points and start and end point of prism

# # Diamond domain
# points.push_back(XY(1.0,0))
# points.push_back(XY(0,1))
# points.push_back(XY(-1,0))
# points.push_back(XY(0,-1))
# domain = CDomainPrism(points,XYZ(0,0,0), XYZ(0,2,0))

#Cube domain
# points.push_back(XY(1.0,0))
# points.push_back(XY(1.0,1))
# points.push_back(XY(-1,1))
# points.push_back(XY(-1,-1))
# points.push_back(XY(1,-1))
# domain = CDomainPrism(points,XYZ(0,0,0), XYZ(0,2,0))


# L domain
# points.push_back(XY(0,0))
# points.push_back(XY(2,0))
# points.push_back(XY(2,1))
# points.push_back(XY(1,1))
# points.push_back(XY(1,2))
# points.push_back(XY(0,2))
# domain = CDomainPrism(points,XYZ(0.5,0,0.5), XYZ(0.5,2,0.5))
# domain = CDomainPrism(points,XYZ(0,0,0), XYZ(0,2,0))

#L domain
# points.push_back(XY(0,0))
# points.push_back(XY(2,0))
# points.push_back(XY(2,1))
# points.push_back(XY(1,1))
# #points.push_back(XY(1.3,1))
# #points.push_back(XY(1,1.3))
# points.push_back(XY(1,2))
# points.push_back(XY(0,2))
# domain = CDomainPrism(points,XYZ(0.5,0,0.5), XYZ(0.5,2,0.5))
# domain = CDomainPrism(points,XYZ(0.5,0,0.5), XYZ(1,2,1))

#T domain
points.push_back(XY(1,0))
points.push_back(XY(0.4,0))
points.push_back(XY(0.3,0.05))
points.push_back(XY(0.15,0.2))
points.push_back(XY(0.1,0.3))
points.push_back(XY(0.1,1))
points.push_back(XY(-0.1,1))
points.push_back(XY(-0.1,0.3))
points.push_back(XY(-0.15,0.2))
points.push_back(XY(-0.3,0.05))
points.push_back(XY(-0.4,0))
points.push_back(XY(-1,0))
points.push_back(XY(-1,-0.1))
points.push_back(XY(1,-0.1))
domain = CDomainPrism(points,XYZ(0,0,0), XYZ(0,2,0))

# Add the domain to the textile
textile.AssignDomain(domain)

# Create a yarn passing through the domain
yarn = CYarn()
yarn.AddNode( CNode(XYZ(0,-0.2,0)))  # x = 1.5 for L
yarn.AddNode( CNode(XYZ(0, 2.2,0)))

# #yarn.AddNode( CNode(XYZ(-1.5,1,-0.05)))
# #yarn.AddNode( CNode(XYZ(1.5,1,-0.05)))

# Add nodes to illustrate domain centreline (T)
#yarn.AddNode( CNode(XYZ(0,0,0))) )
#yarn.AddNode( CNode( XYZ(0,2,0)) )

# Add nodes to illustrate domain centreline (L)
#yarn.AddNode( CNode(XYZ(0.5,0,0.5)))
#yarn.AddNode( CNode(XYZ(0.5,2,0.5)))

section = CSectionEllipse(0.1,0.1)
yarn.AssignSection( CYarnSectionConstant(section))
yarn.SetResolution(10)
textile.AddYarn(yarn)
AddTextile('test', textile)

# Create a voxel mesh for the domain
Vox = CPrismVoxelMesh('CPrismPeriodicBoundaries')
Vox.SaveVoxelMesh( textile, 'PrismVoxels', 20, 20, 20, True, True, NO_BOUNDARY_CONDITIONS, 0, VTU_EXPORT)
