# csv2word

csv2word is a Python library for dealing with word pluralization.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.

```bash
pip install -r requirements.txt
```

## Usage

```python
# Load the CSV into a pandas DataFrame
df = pd.read_csv('sample.csv')  <= update your csv file as input

# Load your Word document
doc = Document('sample.docx')   <= update word file as a output

```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)