from datetime import date
import pandas as pd
import requests 

# import csv

def print_d2k(file_path, mnemonic, datee, value):
    
    f = open(file_path,"w+")

    f.write("TSERIES_START;\n")
    f.write("    CHANGE;\n")
    f.write("    IDENT_START;\n")
    f.write("        DRI_MNEMONIC:\"" + mnemonic + "\";\n")
    f.write("        SERIES_TYPE:\"HIST\";\n")
    f.write("    IDENT_END;\n")
    f.write("    VALUES:\"" + str(datee.strftime("%Y.%m.%d")) + "\" = " + str(value) + ";\n")
    f.write("TSERIES_END;\n")

    f.close()

rates = "https://www.boz.zm/AVERAGE_FXRATES.xlsx"
response = requests.get(rates)

xls = open('ZMB_EXR.xls', 'wb')
xls.write(response.content)
xls = pd.ExcelFile(r"ZMB_EXR.xls")
sheet = xls.parse(0)
# print(type(sheetX.iloc[-1][1]))
# print(sheet.iloc[-1][2])
# print(sheet.iloc[-1][3])
xls.close()

source_date = sheet.iloc[-1][1].date()
# print(source_date)

today = date.today()
# print(today)

if source_date == today:  # checking if date in the source is equal to current day
    buy = sheet.iloc[-1][2]
    sale = sheet.iloc[-1][3]
    print_d2k('outputB.d2k', 'ZMBUSDZMWSPB.F', source_date, buy)
    print_d2k('outputA.d2k', 'ZMBUSDZMWSPA.F', source_date, sale)
else: pass