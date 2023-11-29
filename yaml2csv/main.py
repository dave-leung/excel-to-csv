import os
import yaml
import csv

# Define the input and output directories
input_dir = 'source'
output_dir = 'output'

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Iterate over the files in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith('.yaml'):
        # Read the YAML file
        with open(os.path.join(input_dir, filename), 'r') as file:
            data = yaml.safe_load(file)

        # Extract the 'members' and 'role' data
        bindings = data.get('bindings', [])
        members = []
        role = ''
        for binding in bindings:
            members.extend(binding.get('members', []))
            role = binding.get('role', '')

        # Create the CSV file name based on the YAML file name
        csv_filename = os.path.splitext(filename)[0] + '.csv'

        # Write the data to the CSV file
        with open(os.path.join(output_dir, csv_filename), 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Member', 'Role'])
            for member in members:
                writer.writerow([member, role])
