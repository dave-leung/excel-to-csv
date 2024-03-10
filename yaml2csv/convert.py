import yaml

def read_yaml(file_path, capture_key=None):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)

        if data is not None:
            if capture_key is None:
                print(data)
                return data
            else:
                captured_data = data.get(capture_key)
                print(captured_data)
                return captured_data
        else:
            # Handle the case when the YAML data is None
            print('No captured data found in the YAML file')