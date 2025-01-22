import pandas as pd

def sort_csv_by_video_id(input_file, output_file):
    # Read the CSV file
    df = pd.read_csv(input_file)

    # Ensure the required columns exist
    if 'video_id' not in df.columns or 'element' not in df.columns:
        print("Error: The CSV file must contain 'video_id' and 'element' columns.")
        return

    # Extract numerical part of video_id and create a new column for sorting
    df['video_num'] = df['video_id'].str.extract(r'(\d+)', expand=False).astype(int)

    # Sort the DataFrame by the numerical part of 'video_id'
    sorted_df = df.sort_values(by='video_num', ascending=True).drop(columns=['video_num'])

    # Write the sorted DataFrame to a new CSV file
    sorted_df.to_csv(output_file, index=False)
    print(f"Sorted CSV saved to {output_file}")

# Example usage
input_csv = 'outpt_element.csv'  # Replace with your input CSV file path
output_csv = 'sorted_output2.csv'  # Replace with your desired output file path
sort_csv_by_video_id(input_csv, output_csv)