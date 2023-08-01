from google.cloud import storage
import os
import pandas as pd

# Google Cloud Storage bucket and folder names
bucket_name = ""
source_folder_name = ""
output_folder_name = ""

# Create a client to interact with the Google Cloud Storage
storage_client = storage.Client()

# Get the source bucket
source_bucket = storage_client.bucket(bucket_name)

# List all the blobs (files) in the source folder
blobs = source_bucket.list_blobs(prefix=source_folder_name)

# List to store the names of the converted CSV files
converted_csv_files = []

# Loop through the files
for blob in blobs:
    # Check if the file is an Excel file (xlsx or xls)
    if blob.name.endswith('.xlsx') or blob.name.endswith('.xls'):
        # Generate the output CSV file name by replacing the extension
        csv_filename = os.path.splitext(os.path.basename(blob.name))[0] + '.csv'

        # Read the Excel file from Google Cloud Storage using pandas
        excel_data = blob.download_as_bytes()
        df = pd.read_excel(excel_data)

        # Write the DataFrame to a CSV file
        csv_data = df.to_csv(index=False)

        # Get the output bucket
        output_bucket = storage_client.bucket(bucket_name)

        # Upload the CSV file to Google Cloud Storage in the 'output' folder
        output_file_path = os.path.join(output_folder_name, csv_filename)
        output_bucket.blob(output_file_path).upload_from_string(csv_data, content_type='text/csv')

        # Store the name of the converted CSV file in the list
        converted_csv_files.append(csv_filename)

print("Conversion completed successfully.")
print("CSV files saved in the gs://" + bucket_name + '/' + output_folder_name + " folder on Google Cloud Storage:")
for filename in converted_csv_files:
    print(filename)