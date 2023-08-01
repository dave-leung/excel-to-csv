# excel-to-csv
Convert several Excel files in Google Cloud Storage to csv format using Python library in one time. Then you may use it for loading into Google BigQuery

## Insatllation

*google-cloud-storage* - web application for creating and sharing computational documents

*pandas* - Python library for data analysis and manipulation

```bash
pip3 install pandas
pip3 install google-cloud-storage
```

## How to run

1. Create source and destination folder
2. Place your excel files into source folder
3. modify the paramter as following:
   ```bash
   bucket_name = ""
   source_folder_name = ""
   output_folder_name = ""
   ```
5. Run main.py
