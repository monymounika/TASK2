car={}
print("enter the brand name:")
name=input()
print("enter the color of car:")
color=input()
car[name]=color
print(car)
f=open("./python/TASK_1/output2.txt", "a")
f.write(str(car))
f.close()