from data_capture import read_yaml_file as read_yaml
from data_convertor import convert_to_csv as convert_csv

yaml_file       = "./example/example.yaml"
capture_item    = "tutorial"
csv_file        = "./example/example.csv"

if __name__ == "__main__":
    data = read_yaml(yaml_file,capture_item)
#    convert_csv(data, csv_file)