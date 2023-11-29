import pandas as pd
from docx import Document

# Load the CSV into a pandas DataFrame
df = pd.read_csv('sample.csv')

# Load your Word document
doc = Document('sample.docx')

# For this example, assume the CSV has columns named 'parameter1', 'parameter2', etc.
for index, row in df.iterrows():
    for paragraph in doc.paragraphs:
        if '[date]' in paragraph.text:
            paragraph.text = paragraph.text.replace('[date]', str(row['Date']))
        if '[full_name]' in paragraph.text:
            paragraph.text = paragraph.text.replace('[full_name]', str(row['Full Name']))
        if '[short_name]' in paragraph.text:
            paragraph.text = paragraph.text.replace('[short_name]', str(row['Short Name']))
        if '[title]' in paragraph.text:
            paragraph.text = paragraph.text.replace('[title]', str(row['Title']))
        if '[department]' in paragraph.text:
            paragraph.text = paragraph.text.replace('[department]', str(row['Department']))
        if '[start_date]' in paragraph.text:
            paragraph.text = paragraph.text.replace('[start_date]', str(row['Employee Start Date']))
        if '[company_name]' in paragraph.text:
            paragraph.text = paragraph.text.replace('[company_name]', str(row['Company']))
        if '[location]' in paragraph.text:
            paragraph.text = paragraph.text.replace('[location]', str(row['Location']))
        if '[base_salary]' in paragraph.text:
            paragraph.text = paragraph.text.replace('[base_salary]', str(row['Base Salary']))
        # ... Continue for other parameters ...

# Save the modified document
filename = f"{row['Unit']}_{row['Short Name']} employment verification.docx"
doc.save(filename)
