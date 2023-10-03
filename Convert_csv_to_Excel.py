import pandas as pd
import openpyxl
from openpyxl import load_workbook
from openpyxl.utils.dataframe import dataframe_to_rows

def convert_csv_to_excel(csv_path, sample_excel_path, output_excel_path, column_mapping=None):
    """
    Convert a CSV file to an Excel format based on a sample Excel file.

    Parameters:
    - csv_path: Path to the input CSV file.
    - sample_excel_path: Path to the sample Excel file that provides the format.
    - output_excel_path: Path to save the converted Excel file.
    - column_mapping: Optional dictionary to map CSV columns to Excel columns.
    """
    # Load the data
    csv_data = pd.read_csv(csv_path)
    excel_data = pd.read_excel(sample_excel_path, engine='openpyxl')

    # If no column mapping is provided, assume direct mapping
    if column_mapping is None:
        column_mapping = {col: col for col in csv_data.columns}

    # Create a new dataframe with the structure of the Excel file
    converted_data = pd.DataFrame(columns=excel_data.columns)

    # Fill in the values from the CSV file based on the mapping
    for csv_col, excel_col in column_mapping.items():
        if csv_col in csv_data.columns:
            converted_data[excel_col] = csv_data[csv_col]

    # Fill missing columns with None (Excel's representation of empty data)
    for col in converted_data.columns:
        if col not in column_mapping.values():
            converted_data[col] = None

    # Load the workbook and worksheet
    wb = load_workbook(sample_excel_path)
    ws = wb.active

    # Clear previous data
    for row in ws.iter_rows(min_row=3, max_row=ws.max_row):
        for cell in row:
            cell.value = None

    # Append new data
    for r_idx, row in enumerate(dataframe_to_rows(converted_data, index=False, header=False), 3):
        for c_idx, value in enumerate(row, 1):
            ws.cell(row=r_idx, column=c_idx, value=value)

    # Save to the output file
    wb.save(output_excel_path)

    return output_excel_path

# Example usage of the function
convert_csv_to_excel("./Practical 2/PHY151_Pods_Prac2_SAMPLE.csv", "./Sample Pods File.xlsx", "./Converted_Pods_File_Function.xlsx")

