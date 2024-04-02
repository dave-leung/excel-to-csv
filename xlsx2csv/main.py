from cloud_upload import upload_to_cloud as upload_cloud
from data_convertor import convert_to_csv as convert_csv

# Google Cloud Storage bucket and folder names
bucket_name = "example_bucket"
file_name   = "example.xlsx"

if __name__ == "__main__":
    csv_files = convert_csv(bucket_name,file_name)
    upload_cloud(bucket_name,csv_files)