import pandas as pd



# save filepath to variable for easier access


melbourne_file_path = 'd:/Git/AI/Kagel/melb_data.csv'
#melbourne_file_path = 'melb_data.csv'

# read the data and store data in DataFrame titled melbourne_data
#melbourne_data = pd.read_csv(melbourne_file_path, index_col="price")
melbourne_data = pd.read_csv(melbourne_file_path)
print(melbourne_data.head(5))

##melbourne_data.head()
##print(sum(melbourne_data('Price')))
# print a summary of the data in Melbourne data
melbourne_data.describe()