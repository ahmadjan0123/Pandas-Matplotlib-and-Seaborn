# data frame
import pandas as pd
data1 = ({
    'Name':['AHMAD','ALI','AHAD'],
    'MARKS':[10,15,20],
    'ATTENDANCE':[80,72,68]
})

DF1 = pd.DataFrame(data1)


# from list

students = (
    ['AHMAD','ALI','HAMMAD'],
    [12,13,15],
    [22,25,12]
)

DF2 = pd.DataFrame(
    students,
    columns=['NAME','MARKS','ATTENDANCE']
)

print(DF2)


print(DF2.shape)

DF2.info()


# practice - 1
p1 = pd.DataFrame({
    'Name': ['Ahmad','Ali','Sara'],
    'Age':[20,21,19]
})

print(p1)


# practice 2
print(p1.shape)

#practice - 3
print(p1['Age'])

#practice -4
print(p1[['Name','Age']])


#practice -5
p1.info()

#practcie - 6
p1.describe