#!/usr/bin/env python3
"""
Script to split CSV files into batches of 50 rows each.
Each batch will include the header row.
"""

import csv
import os
from pathlib import Path

def split_csv_file(input_file, batch_size=50):
    """Split a CSV file into batches of specified size."""
    input_path = Path(input_file)
    output_dir = input_path.parent
    
    # Read the CSV file
    with open(input_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)  # Read header row
        rows = list(reader)
    
    # Calculate number of batches needed
    total_rows = len(rows)
    num_batches = (total_rows + batch_size - 1) // batch_size  # Ceiling division
    
    print(f"Splitting {input_path.name} ({total_rows} rows) into {num_batches} batches...")
    
    # Create batches
    for batch_num in range(num_batches):
        start_idx = batch_num * batch_size
        end_idx = min(start_idx + batch_size, total_rows)
        batch_rows = rows[start_idx:end_idx]
        
        # Create output filename
        base_name = input_path.stem
        output_file = output_dir / f"{base_name}_batch{batch_num + 1}.csv"
        
        # Write batch to file
        with open(output_file, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header)  # Write header
            writer.writerows(batch_rows)  # Write batch rows
        
        print(f"  Created {output_file.name} with {len(batch_rows)} rows")
    
    return num_batches

def main():
    """Main function to process all CSV files in local-files directory."""
    local_files_dir = Path(__file__).parent / "local-files"
    
    if not local_files_dir.exists():
        print(f"Error: {local_files_dir} directory not found!")
        return
    
    # Find all CSV files
    csv_files = list(local_files_dir.glob("*.csv"))
    
    if not csv_files:
        print(f"No CSV files found in {local_files_dir}")
        return
    
    print(f"Found {len(csv_files)} CSV file(s) to process\n")
    
    # Process each CSV file
    for csv_file in sorted(csv_files):
        split_csv_file(csv_file, batch_size=50)
        print()
    
    print("All files processed successfully!")

if __name__ == "__main__":
    main()

