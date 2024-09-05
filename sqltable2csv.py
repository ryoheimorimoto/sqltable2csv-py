import pandas as pd
import sys

def convert_sql_result_to_csv(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    headers = [header.strip() for header in lines[0].split('|')]

    data = []
    for line in lines[3:]:
        row = [item.strip() for item in line.split('|')]
        data.append(row)

    df = pd.DataFrame(data, columns=headers)
    df.to_csv(output_file, index=False)
    print(f"Data has been saved to {output_file}.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python sqltable2csv.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    convert_sql_result_to_csv(input_file, output_file)
