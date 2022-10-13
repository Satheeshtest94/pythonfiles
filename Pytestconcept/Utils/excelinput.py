import openpyxl
from openpyxl import Workbook

def handling():

    path = "/Pytestconcept/Input file/input file.xlsx"

    new_book = openpyxl.load_workbook(path)


    new_sheet = new_book.active
    # data  = new_sheet.cell(row =1 ,column=1)
    # print(data.value)
    # print(new_sheet.max_row)
    max_row = new_sheet.max_row
    max_col = new_sheet.max_column
    # print(new_sheet.max_column)
    for row in range(1,(max_row)+1):
        for column in range(1,(max_col)+1):
            cell_value = new_sheet.cell(row = row,column=column)
            print(cell_value.value,end = "")
        print()

    new_book.save(path)



handling()
