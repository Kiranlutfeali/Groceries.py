import pandas
csv_filepath = "products.csv"
df = pandas.read_csv(csv_filepath)
print(type(df)) #> <class 'pandas.core.frame.DataFrame'>
# todo: assemble a list of dictionaries
# APPROACH A
#products = []
#
#for row in _____________: # how to loop through each row in a dataframe
#    products.append({}) # how to convert each row to a dictionary
# APPROACH B
products = df.to_dict("records")

