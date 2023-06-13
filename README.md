# EXCEL TO CSV CONVERTER

Python script made to convert excel into csv.

The current implementation will generate a csv file with headers and delimited by ```;```

Setup Instruction:
1. Run ```pip install -r requirements.txt``` to install dependencies.
2. Copy ```conf.tmpl.json``` and create ```conf.json``` in the project root directory. Fill the field according to your environment.

## Running The Script
Inside ```conf.json``` there are 2 mandatory fields to be filled: 
1. The ```input_file_path``` is the path to the excel file to be converted. 
2. The ```output_file_path``` is the path to the csv result.

Run ```python main.py``` to start the process