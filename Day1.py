print("hello world")
name ="RAM"
facualty = "computer science"
dob= "01/01/2000"
print(f"hello,{name} you are a student of {facualty} your date of birth is:{dob}.")




#check datatypes
print(f"type of name:{type(name)}")#str
print(f"type of name:{type(facualty)}")#str
print(f"type of name:{type(dob)}")#str
    
    #swap variable easily 
x = 10
y = 20

print("valu after swap:", x, y)

x, y = y, x
print("After swap:x=",x,"y=",y)