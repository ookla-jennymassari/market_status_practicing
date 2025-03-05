from IPython.display import display
import pandas as pd

table = pd.read_excel("Market_Status_Info_Report_2025-01-23.xlsx")
display(table)

market_column = table['Market']
print(market_column)

type_column = table['Type']
print(type_column)