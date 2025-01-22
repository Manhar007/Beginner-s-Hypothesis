import pandas as pd

def sort_csv_by_video_id(input_file, output_file):
    try:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(input_file)

        # Check if 'video_id' column exists
        if 'video_id' not in df.columns:
            print("Error: 'video_id' column not found in the CSV file.")
            return

        # Sort the DataFrame by the 'video_id' column
        df_sorted = df.sort_values(by='video_id')

        # Write the sorted DataFrame to a new CSV file
        df_sorted.to_csv(output_file, index=False)

        print(f"CSV file sorted successfully. Sorted file saved as '{output_file}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Replace 'input.csv' with the path to your unsorted CSV file
# Replace 'output.csv' with the path where you want the sorted file to be saved
input_file = 'self_test_summary.csv'
output_file = 'outpt_element.csv'
sort_csv_by_video_id(input_file, output_file)
