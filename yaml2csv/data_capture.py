import yaml

def read_yaml_file(file_path, capture_key=None):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)

        if data is not None:
            if capture_key is None:
#                for keys in data.items():
#                    print(keys)
                print(data)
                return data
            else:
                captured_item = data.get(capture_key)
                dict = {capture_key: captured_item}
                print(dict)
                return dict
        else:
            # Handle the case when the YAML data is None
            print('No captured data found in the YAML file')