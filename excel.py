from win32com.client import Dispatch

def get_workbook(path):
    xl = Dispatch('Excel.Application')
    xl.Visible = 1
    return xl.Workbooks.open(path)

wb = get_workbook(r'c:\temp\test.xlsx')
sheet = wb.Worksheets.Item(1)
sheet.Range('A1').Value2 = 'test'

del wb, sheet