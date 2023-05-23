a=[1,2,3,4]
b=['a','b','c','d','e']
c=['*','*','*']

for i in zip(a,b,c):
    print(i) 
    
print("___________________________")
    
for i,z,x in zip(a,b,c):
    print(i)
    print(z)
    print(x)

print("___________________")    
new=[i for i in a]
print(new)