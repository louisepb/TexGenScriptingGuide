# DryTextileExport.py
# Generates conformal mesh of just the yarns and
# creates ABAQUS input file

textile = GetTextile()
weave = textile.GetWeave()

# Set the number of layers in the section mesh
# First parameter specifies number of layers (must be even number)
# Second parameter defaults to True to give triangular elements at corners
# producing wedge elements. False to force all 4 noded elements, 
# producing all hex elements

sectionMesh = CSectionMeshRectangular (4,True)
weave.AssignSectionMesh(sectionMesh)


# Set up any x,y,z transformations
tension = CLinearTransformation()
tension.AddScale( 1.1, 1, 1)

# Setup class which generates ABAQUS files with conformal wedge/hex elements
deformer = CSimulationAbaqus()  
deformer.SetIncludePlates( False )  # Whether or not to include compression plates
deformer.AddDeformationStep(tension)

fName = 'ExportDry'
bRegenerateMesh = False;  # True if want to regenerate mesh after intersection correction
bElementType = False   # True for C3D8, False for C3D8R
bAdjustIntersections = False
Tolerance = 1e-6;
deformer.CreateAbaqusInputFile(textile, fName, bRegenerateMesh , bElementType, bAdjustIntersections, Tolerance )
