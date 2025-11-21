# Figure out a way to store 9 & 9.0 as separate values in the set. (You can take help of built-in data types)

# First way
values={9, "9.0"}
print(values)

# Second way
values={
    ("float", 9.0), 
    ("int", 9)
}
print(values)