import pandas as pd
import pyproj

# Conversion function
def convert_coordinates(input_file, output_file, col_name_one, col_name_two):
    # From to (ESRI number)
    transformer = pyproj.Transformer.from_crs("EPSG:3776", "EPSG:22763", always_xy=True)

    # Read file
    df = pd.read_csv("coords.csv")

    # Columns must be labelled 'E' and 'N' to work
    df[out_one], df[out_two] = transformer.transform(df['E'].values, df['N'].values)

    # Export as a CSV
    # Change the column names as you will.
    df[[out_one, out_two]].to_csv(output_file, index=False)


out_one = 'Latitude' # name of output
out_two = 'Longitude' # name of output


# Calling function
convert_coordinates('input_coordinates.csv', 'output_coordinates.csv',out_one,out_two)