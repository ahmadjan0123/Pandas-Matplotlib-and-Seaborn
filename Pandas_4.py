import pandas as pd

df = pd.DataFrame({
    "Name":["Ahmad","Ali","Sara","Fatima","Bilal"],
    "Age":[20,21,19,22,20],
    "Marks":[88,75,95,67,91],
    "City":["Peshawar","Lahore","Islamabad","Peshawar","Lahore"]
})

print(df)

print(df.loc[3,'Name'])

print(df['Age']>=20)

print(df[df['Marks']>90])
print(df['Marks']>90)

print(df[df['Age']>=20 & (df['Marks']>=50)])


print(df[  
    ~(df['City']=="Lahore")
])

print(df[ 
    df['City'].isin(['Lahore','Peshawar'])
])

print(df[  
    df["Marks"].between(80,90)
])

print(df.query('Marks > 50 and Age>50'))

print(df.sort_values(['City','Age']))

print(df[df['Marks']>90][['Name']])


# PRACTICE PROBLEM

df[(df['Age']==20)]
df[(df['Marks']>=90)]
df[(df['Marks']<=80)]

# problem - 3
print(df[df['City']=='Lahore'])
print(df[~(df['City']=='Lahore')])

#problem - 4


print(df[(df['Age']>20) & (df['Marks']>70)])
print(df[(df['Age']==20) | (df['Marks']>90)])

#problem - 5
print(df[df['City'].isin(['Lahore','Islamabad'])])

# problem - 6
print(df[df['Marks'].between(70,90)])

#problem - 7
print(df.query('Age>20 and Marks>80'))

#problem - 8
df.sort_values(
    'Marks' ,
     ascending=False

)
df.sort_values(
    'Marks' ,
     ascending=True

)

df.sort_values(['City','Marks'])

#problem - 9
print(df.nlargest(3,'Marks'))

df.nsmallest(2,"Marks")