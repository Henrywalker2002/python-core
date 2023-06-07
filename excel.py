import pandas as pd 

# df = pd.read_csv('cities.csv')
# print(df)

df = pd.read_excel("file_example_XLS_50.xls", "Sheet1", index_col= 'Id')
df = df.drop(columns=[0])

new_df = df[df.Country == "France"]

new_df.to_csv("france.csv")
df['Full Name'] = df['First Name'] + ' ' + df['Last Name']
df = df.drop(columns= ['First Name', 'Last Name'])
print(df)