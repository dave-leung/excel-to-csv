import csv

def convert_to_csv(data, filename):
    if not data:
        print("Data is empty. Nothing to convert.")
        return
    
    field_names = ['key', 'value']  # Define the field names for the CSV
    
    with open(filename, 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(field_names)  # Write the field names as the header
        
        for item in data:
            writer.writerow(item)  # Write each item as a row in the CSV