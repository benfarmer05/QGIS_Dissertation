import os
from qgis.core import QgsProject, QgsRasterLayer, QgsCoordinateReferenceSystem
from qgis import processing
from qgis.utils import iface

def resample_rasters(input_gdb_path, output_folder, target_resolution):
    # Ensure output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Initialize QGIS application if running outside QGIS
    from qgis.core import QgsApplication
    qgs = QgsApplication([], False)
    qgs.initQgis()
    
    # Load the ESRI geodatabase
    QgsProject.instance().addMapLayer(QgsRasterLayer(input_gdb_path, "TempLayer"))
    
    # Get all raster layers
    layers = QgsProject.instance().mapLayers().values()
    
    for layer in layers:
        if isinstance(layer, QgsRasterLayer):
            layer_name = layer.name()
            output_raster_path = os.path.join(output_folder, f"{layer_name}_resampled.tif")
            
            # Get the CRS and dimensions
            crs = layer.crs().authid()
            width, height = layer.width(), layer.height()
            x_res = target_resolution
            y_res = target_resolution
            
            # Perform resampling
            processing.run(
                "gdal:warpreproject",
                {
                    'INPUT': layer.dataProvider().dataSourceUri(),
                    'TARGET_CRS': crs,
                    'RESAMPLING': 0,  # Nearest neighbor, change if needed
                    'X_RESOLUTION': x_res,
                    'Y_RESOLUTION': y_res,
                    'OUTPUT': output_raster_path
                }
            )
            
            print(f"Resampled raster saved to: {output_raster_path}")

    # Exit QGIS application if running outside QGIS
    QgsApplication.exitQgis()

if __name__ == "__main__":
    input_gdb_path = '/Users/benja/Documents/Farmer_Ben_Dissertation/QGIS_Dissertation/data/Bathymetry/NOAA_LIDAR_Blondeau/US_Caribbean_Bathy_Mocaics.gdb'
    output_folder = '/Users/benja/Documents/Farmer_Ben_Dissertation/QGIS_Dissertation/output'
    target_resolution = 50  # target resolution in meters
    resample_rasters(input_gdb_path, output_folder, target_resolution)
