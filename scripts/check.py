import pandas as pd

def compare_column_values(file1, file2, column_name):
    try:
        # Read the CSV files into DataFrames
        df1 = pd.read_csv(file1)
        df2 = pd.read_csv(file2)

        # Check if the specified column exists in both files
        if column_name not in df1.columns or column_name not in df2.columns:
            print(f"Error: Column '{column_name}' not found in one or both files.")
            return

        # Get the values from the specified column in both DataFrames
        values1 = set(df1[column_name])
        values2 = set(df2[column_name])

        # Find the differences between the two sets of values
        diff1 = values1 - values2
        diff2 = values2 - values1

        # Count the number of differences
        num_diff = len(diff1) + len(diff2)

        print(f"Number of different values in column '{column_name}': {num_diff}")
        print(f"Values in '{file1}' but not in '{file2}': {diff1}")
        print(f"Values in '{file2}' but not in '{file1}': {diff2}")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Replace 'file1.csv' and 'file2.csv' with the paths to your CSV files
# Replace 'column_name' with the name of the column to compare
file1 = 'elements.csv'
file2 = 'BH25\\Training_Data\\train.csv'
column_name = 'element'
compare_column_values(file1, file2, column_name)
