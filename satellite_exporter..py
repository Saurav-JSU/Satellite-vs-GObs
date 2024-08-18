import ee

class DataExporter:
    def __init__(self, aoi_id, dataset_id, parameters, start_year, end_year):
        # Initialize the Earth Engine
        ee.Initialize()
        
        # Set instance attributes
        self.AOI = ee.FeatureCollection(aoi_id)
        self.dataset_id = dataset_id
        self.parameters = parameters
        self.start_year = start_year
        self.end_year = end_year

    def export_data(self):
            # Access the dataset
            dataset = ee.ImageCollection(self.dataset_id)
            
            # Loop through years and parameters for data export
            for year in range(self.start_year, self.end_year + 1):
                for parameter in self.parameters:
                    
                    # Set up the time range
                    start_date = ee.Date.fromYMD(year, 1, 1)
                    end_date = ee.Date.fromYMD(year + 1, 1, 1)
                    
                    # Filter dataset for the given time range and select the parameter
                    filtered_collection = dataset.filterDate(start_date, end_date).select(parameter)
                    
                    # Define a function for mapping over the filtered collection
                    def map_function(image):
                        return image.reduceRegions(
                            reducer=ee.Reducer.mean().setOutputs([parameter]),
                            collection=self.AOI,
                            scale=250
                        ).map(lambda feature: feature.set('imageId', ee.String(image.id())))
    
                    # Flatten the results and prepare for export
                    feature_collection = filtered_collection.map(map_function).flatten()
    
                    selectors = [parameter, 'imageId', 'CONAME']
                    
                    # Set up the export task
                    task = ee.batch.Export.table.toDrive(
                        collection=feature_collection,
                        description=f'{parameter}_{year}',
                        folder='GEE_MS_temp',
                        fileNamePrefix=f'{parameter}_{year}',
                        fileFormat='CSV',
                        selectors=selectors
                          # Add other needed properties
                    )
                    task.start()
                    print(f'Exporting {parameter} for year {year} to Drive...')
    
exporter = DataExporter(
    'location_of_asset',
    "gee_image_collection",
    [
     'parameter_name'
    ],
    1980,
    2023
)
exporter.export_data()
