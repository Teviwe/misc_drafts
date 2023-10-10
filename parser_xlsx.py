import sys
import openpyxl
from tabulate import tabulate

def parse_sheet(file_path, sheet_name):
    workbook = openpyxl.load_workbook(file_path, data_only=True)
    sheet = workbook[sheet_name]

    data = []
    for row in sheet.iter_rows(values_only=True):
        row_data = []
        for cell_value in row:
            if isinstance(cell_value, str) and cell_value.startswith('='):
                try:
                    cell_value = sheet[cell_value[1:]].value
                    # Handle division by zero error
                    if isinstance(cell_value, (int, float)) and cell_value == 0:
                        cell_value = "DIV/0"
                except Exception:
                    cell_value = "ERROR"
            row_data.append(cell_value)
        data.append(row_data)

    workbook.close()

    table = tabulate(data, headers='firstrow', tablefmt='grid')
    print(table)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script_name.py path/to/your/file.xlsx sheet_name")
        sys.exit(1)

    excel_file_path = sys.argv[1]
    sheet_name = sys.argv[2]
    parse_sheet(excel_file_path, sheet_name)
