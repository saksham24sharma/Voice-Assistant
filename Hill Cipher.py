import numpy


alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
arr = numpy.array([],[])
plain_arr=[]
key_indx =[]
ans = []

key =list(input("Enter key : "))

for i in key:
    key_indx.append(alpha.index(i))

a = numpy.array(key_indx)
b = a.reshape(2,2)

#print(b)

plain = list(input("Enter plaintext : "))
for j in plain:
    plain_arr.append(alpha.index(j))

c = len(plain)
if (c % 2 == 0):
    block = c//2
    e = numpy.array(plain_arr).reshape(block, 2)
    arr = numpy.dot(e,b)
    print(arr)
else:
    plain_arr.append(23)
    block = len(plain_arr)//2
    e = numpy.array(plain_arr).reshape(block,2)
    arr = numpy.dot(e,b)
   # print(arr)

for row in range(0,block):
    for col in range(0,2):
        ans.append(arr[row][col])

for l in ans:
    temp = l%26
    print(alpha[temp],end='')
