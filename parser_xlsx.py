import sys
import argparse
import pandas as pd

def list_sheets(file_path):
    try:
        sheets = pd.read_excel(file_path, sheet_name=None)
        return list(sheets.keys())
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return []

def parse_sheet(file_path, sheet_name):
    try:
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        df = df.fillna("None")  # Replace NaN values with "NaN"
        print(df.to_string(index=False))
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except KeyError:
        print(f"Sheet '{sheet_name}' does not exist in the Excel file.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Excel Parser")
    parser.add_argument("file_path", help="Path to the Excel file")
    parser.add_argument("--sheet", help="Name of the sheet to parse")
    args = parser.parse_args()

    excel_file_path = args.file_path

    # List available sheets
    available_sheets = list_sheets(excel_file_path)
    print("Available sheets in the Excel file:")
    for i, sheet in enumerate(available_sheets):
        print(f"{i+1}. {sheet}")

    # Select sheet to parse
    if args.sheet:
        sheet_name = args.sheet
    else:
        sheet_option = input("Enter the number of the sheet to parse (or enter the sheet name manually): ")
        try:
            sheet_index = int(sheet_option) - 1
            if sheet_index >= 0 and sheet_index < len(available_sheets):
                sheet_name = available_sheets[sheet_index]
            else:
                raise ValueError
        except ValueError:
            sheet_name = sheet_option

    # Check if the specified sheet exists and parse it if it does
    if sheet_name in available_sheets:
        parse_sheet(excel_file_path, sheet_name)
    else:
        print(f"Sheet '{sheet_name}' does not exist in the Excel file.")
