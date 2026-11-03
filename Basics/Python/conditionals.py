#if-else

a = 5

if a < 20:
    print("small")
elif a > 20:
    print("big")
else:
    print("error")
    
    
    
    
    
# nested if 
"""
if(condition 1){
    if(condition){
        
    }
    else{
        
    }
}
else{
    if(condition){
        
    }
    else{
        
    }
}

"""


"""
b = "hello"
a = [1,2,3,4,5]

for item in a:
    print(item)

print("a" in "hello")   # will give false


# print 1 to 1000 and print both 1 and 1000
for i in range(1, 1001):
    print(i)
"""
    
# break-continue 

a = [1,2,3,4,"a",5,6,7]

for i in a:
    if type(i) == type("b"):
        break
    else:
        print(i)
        
print("-------------")

for i in a:
    if type(i) == type("a"):
        continue
    else:
        print(i)

print("---------------")

a = [1,2,3,4,5]
result = 0

i = 0

n = len(a)
while i<n:
    result = result + a[i]
    i+=1
    
print(result)

print("--------")

a = [-10, 2, 19, -3, -8]

a.sort(reverse=True)

print(a)

#