import arcpy
arcpy.env.workspace = 'C:/data'
input_fc = 'County'
output_fc = 'County_new'
out_coordinate_system = arcpy.SpatialReference('NAD 1983 StatePlane Missouri East FIPS 2401 (US Feet)')
arcpy.Project_management(input_fc, output_fc, out_coordinate_system)

