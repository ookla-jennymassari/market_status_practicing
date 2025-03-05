from IPython.display import display
import pandas as pd


# Read and display the whole table
data = pd.read_excel("Market_Status_Info_Report_2025-01-23.xlsx")
display(data)

# Display all columns names
all_columns = list(data.columns)
# print(all_columns)

# Sorting the columns with sorted() function
sorted_columns = sorted(data.columns)
print(sorted_columns)


# Display only one column
market_column = data['Market']
# print(market_column)

type_column = data['Type']
# print(type_column)

#Display multiple columns
market_type_column = data[['Market', 'Type']]
# print(market_type_column)


