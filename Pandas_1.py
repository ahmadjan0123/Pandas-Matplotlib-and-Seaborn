import pandas as pd

#question - 1
p1 = pd.Series([10,20,30,40])
print(p1)

#question - 2
p2 = pd.Series(
    [85,90,78],
    index=['Ali','Sara','Ahmad']
)
print(p2)

# question -3 
print(p2['Sara'])

#question - 4

dict = {
    "Apple":120,
    "Banana":80,
    "Orange":150
}

p4 = pd.Series(dict)

print(p4)

# question - 5

marks = pd.Series([55,72,88,40,91])

# Print only marks greater than 70.

print(marks[marks>70])


e1 = pd.Series(['ahmad','ali','hammad'])