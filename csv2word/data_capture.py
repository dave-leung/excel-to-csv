import pandas as pd

def read_csv_file(csv_file):
    df = pd.read_csv(csv_file)
    column_names = list(df.columns)
    return column_names