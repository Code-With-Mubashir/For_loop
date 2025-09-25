# For_Loop
# Example No.01
items = ["apple", "banana", "cherry"]

for item in items:
    print(item)
    
    
# Example No.02
number = (1,2,3,4,5,6,7)
for num in number:
    print(num)
    
# Example No.03
name = {"Robert","John","Michael"}
for nam in name:
    print(nam)
    
# Nested Loop
# Example No.01
names = ["Alice", "Bob"]
hobbies = ["Reading", "Cycling"]
for name in names:
    for hobby in hobbies:
        print(f"{name} enjoys {hobby}")
    
# Example No.02
rows = 3
for i in range(1,rows+1):
    for j in range(1,i+1):
        print("*",end=" ") 
    print()
    
    
# Loop Control Statemet
# 1. Break statement
# Example No.01
for i in range(1, 11):
    if i == 5:
        break
    print(i)
    
# Example No.02
for i in range(6):
    if i == 4:
        break
    print(i)
    
# Example No.03
for char in "Hello, World!":
    if char == ",":
        break
    print(char)
    
# 2. Continue statement
# Example No.01
for i in range(1, 11):
    if i == 5:
        continue
    print(i)
    
# Example No.02
for i in range(6):
    if i == 4:
        continue
    print(i)
    
# Example No.03
for char in "Hello, World!":
    if char == ",":
        continue
    print(char)
    
# 3.Pass statement
# Example No.01
for i in range(1, 6):
    if i == 3:
        pass
    else:
        print(i)
        
# Example No.02
for i in range(1, 6):
    if i == 3:
        pass
    print(i)
    
# Example No.03
for char in "Hello":
    if char == "l":
        pass
    print(char)
    

        
        
  
    