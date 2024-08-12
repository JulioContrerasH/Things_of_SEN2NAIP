# read geojson and extract the coordinates
import geopandas as gpd

file_path = 'data/vector/CombinedGeoJson.geojson'
gdf = gpd.read_file(file_path)

# Insert a column ROI name and assign the value 'ROI_0000', 'ROI_0001' etc
gdf['id'] = ['ROI_'+str(i).zfill(4) for i in range(len(gdf))]

# Extract the coordinates and assign to a new columns x and y
gdf['x'] = gdf['geometry'].x
gdf['y'] = gdf['geometry'].y

# Delete columns x and y
gdf = gdf.drop(columns=['Name'])


# Save the data to a new geojson file
gdf.to_file('data/vector/Points.geojson', driver='GeoJSON')

# Print key y values in diccionary format keys:ROI column and values: x, y columns
print(gdf[['ROI', 'x', 'y']].to_dict(orient='records'))