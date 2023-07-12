# EXCEL TO CSV CONVERTER

Python script made to convert excel into csv.

The current implementation will generate a csv file with headers.

Setup Instruction:
1. Run ```pip install -r requirements.txt``` to install dependencies.
2. Copy ```conf.tmpl.json``` and create ```conf.json``` in the project root directory. Fill the field according to your environment.

## Running The Script
Configure ```conf.json```: 
1. The ```input_file_path``` is the path to the excel file to be converted. 
2. The ```output_file_path``` is the path to the csv result.
3. You can configure specific columns to get by setting ```column_idx``` to an array e.g. ```[0, 1, 2, 3]```. The index starts from 0, meaning the example shown will take the 1st until the 4th column. To get all column simply set it to an empty array i.e. ```[]```
4. Set the ```sheet_number``` to configure from which sheet the program will read. The number starts from 0, being the first sheet.
5. Set the ```delimiter``` to configure which delimiter to use in the resulting CSV.


Run ```python main.py``` to start the process