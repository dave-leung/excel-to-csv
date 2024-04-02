from docx import Document

def convert_to_document(file, data):
    # Read the data from the file
    with open(file, 'r') as f:
        lines = f.readlines()
    
    # Import the values into the Word document
    for line in lines:
        # Split the line into key and value
        key, value = line.strip().split(',')
    
        # Add the key and value to the document
        document.add_paragraph(f'{key}: {value}')
    
    # Save the document
    document.save(data)