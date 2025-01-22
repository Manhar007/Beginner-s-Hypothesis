import pandas as pd

# Load the CSV file
file_path = 's2.csv'  # Replace with the path to your CSV file
df = pd.read_csv(file_path)

# Define the rounding function
def custom_round(value):
    if abs(value - 6.9) < abs(value - 9.6):
        return 6.9
    else:
        return 9.6

# Apply the rounding function to the 'speed' column
df['speed'] = df['speed'].apply(custom_round)

# Save the updated dataframe back to a new CSV file
output_path = 'rounded_speeds.csv'  # Specify the output file name
df.to_csv(output_path, index=False)

print(f"Updated CSV saved to: {output_path}")
