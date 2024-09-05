# SQL Table to CSV Converter

This Python script converts SQL query results in a text file format into a CSV file. The input file must have data separated by pipes (`|`), and the first row should contain the column headers.

## Usage

### Command

To run the script, use the following command:

```bash
python sqltable2csv.py <input_file> <output_file>
```

### Example
```bash
python sqltable2csv.py input.txt output.csv
```

This command reads the SQL result from data.txt and saves the output to output.csv



## Input File Format

The input file should be formatted as follows:

- The first line contains the headers.
- The data rows start from the fourth line.
- Data should be separated by pipes (|).

### Example

```
id | name       | age | city
----|------------|-----|---------
1   | Alice      | 30  | New York
2   | Bob        | 25  | Los Angeles
3   | Charlie    | 35  | Chicago
4   | Diana      | 28  | Houston
5   | Edward     | 40  | Phoenix
```

## Requirements

You need to have the following Python package installed:

- pandas

You can install it using the following command:

```bash
pip install -r requirements.txt
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
