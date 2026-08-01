import pandas as pd

data = {
    "Name": ["Ahmad", "Ali", "Sara", "Usman", "Ali"],
    "Age": [20, 22, 19, 23, 22],
    "Marks": [88, 75, 95, 70, 75],
    "Department": ["AI", "CS", "AI", "SE", "CS"]
}

df = pd.DataFrame(data)

print(df)


print(df.sort_values(by='Marks',ascending=False))


print(df.sort_values(by=['Department','Marks']))


data1 = {
    "Student": ["A", "B", "C", "D", "B", "E"],
    "Marks": [88, 70, 95, 65, 70, 82],
    "Department": ["AI", "CS", "AI", "SE", "CS", "AI"]
}

df1 = pd.DataFrame(data1)



print(df1.sort_values(by='Marks',ascending=True))


print(df1.sort_values(by='Marks',ascending=False))

print(df1['Marks'].rank())



df1 = df1.drop_duplicates()

print(df1.duplicated())

print(df1['Department'].nunique())

print(df1["Department"].value_counts())

print(df1.nlargest(3,'Marks'))

print(df1.nsmallest(3,'Marks'))


print(df1['Department']=='AI')

