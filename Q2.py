
import pandas as pd                                   
num = int(input("Enter Range : "))   
inputs=[]
power=[]       
for i in range(num):
    n=int(input("enter a number:"))                                                          
    inputs.append(n)                             
    power.append(n*n)    
output=pd.Series(power,index=[inputs])         
print(output)                        
