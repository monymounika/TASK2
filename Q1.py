import pandas as pd
s1 = pd.Series([10,9,8,7,6])
s2 = pd.Series([5,4,3,2,1])
print("first series:")
print(s1)
print("second series:")
print(s2)
s=s1 + s2
print("Add both series:")
print(s)
s=s1 - s2
print("Subtract both series:")
print(s)
s=s1 * s2
print("Multiply both series:")
print(s)
s=s1 / s2
print("Divide both series:")
print(s)
s=s1 // s2
print("Floor division of both series:")
print(s)






