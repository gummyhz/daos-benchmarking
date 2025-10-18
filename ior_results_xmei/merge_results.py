import pandas as pd
import glob
import os

# Directory containing the CSV files
input_dir = "ior-results-w_n-1_seg-32_20251017_48core-skip1"
seg = int(input_dir.split('seg-')[1].split('_')[0])

# Get list of all CSV files
csv_files = glob.glob(os.path.join(input_dir, '*.csv'))

# Initialize an empty list to store dataframes
dfs = []

# Process each CSV file
for file in csv_files:
    # Read the CSV file
    df = pd.read_csv(file)  
    # Extract nodes and transfer size from filename
    filename = os.path.basename(file)
    # Example filename: write_n-1_ppn-8_tx-16K.csv
    nnodes = int(filename.split('n-')[1].split('_')[0])
    # Add new columns
    df['nnodes'] = nnodes
    df['seg']   = seg 
    # Append to our list of dataframes
    dfs.append(df)

# Combine all dataframes
merged_df = pd.concat(dfs, ignore_index=True)

# Convert bandwidth from MiB/s to GiB/s
merged_df['bw(GiB/s)'] = merged_df['bw(MiB/s)'] / 1024.0
merged_df = merged_df.drop('bw(MiB/s)', axis=1)  # Remove the old column

# Sort the dataframe
merged_df = merged_df.sort_values(['nnodes', 'xfer(KiB)'])

# Save the merged results
output_file = 'merged_ior_results.csv'
merged_df.to_csv(output_file, index=False)

print(f"Merged results saved to {output_file}")
