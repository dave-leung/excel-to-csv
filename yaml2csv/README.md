# yaml2csv

yaml2csv is a Python library for convert yaml file into csv formated.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install -r requirements.txt
```

## Usage

Update the file path and search_key here (ignore the capture_item if you want to convert all the file). However, you need to remove the capture_item in read_yaml.
```python
yaml_file       = "./example/example.yaml"
capture_item    = "company"
csv_file        = "./example/example.csv"
```

```python
read_yaml(yaml_file) <= remove capture_item here
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)