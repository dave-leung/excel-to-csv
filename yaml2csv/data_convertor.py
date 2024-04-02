import csv

def convert_to_csv(keys, values, filename):
    if not keys or not values:
        print("Data is empty. Nothing to convert.")
        return
    
    field_names = ['key', 'value']  # Define the field names for the CSV
    
    with open(filename, 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(keys)  # Write the field names as the header
        
        for item in values:
            writer.writerow(item)  # Write each item as a row in the CSV