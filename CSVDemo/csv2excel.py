import csv
import openpyxl


def csv_to_excel(csv_filename, excel_filename):
    # Read CSV file
    csv_data = []
    with open(csv_filename) as f:
        csv_data = [row for row in csv.reader(f)]

    # Write to Excel file
    workbook = openpyxl.workbook.Workbook()
    worksheet = workbook.active
    for row in csv_data:
        worksheet.append(row)
    workbook.save(excel_filename)


if __name__ == "__main__":
    csv_to_excel("my_file.csv", "my_file.xlsx")