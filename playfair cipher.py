import re
key = input("Enter plain text: ")
alpha = ['a','b','c','d','e','f','g','h','i','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
arr = []


for k in key:
    if(k not in arr):
        arr.append(k)

for el in alpha:
    if(el not in arr):
        arr.append(el)


print("[" + arr[0]+"," + arr[1]+","  + arr[2]+","  + arr[3] +"," + arr[4] + "]")
print("[" + arr[5] +"," + arr[6] +"," + arr[7]+","  + arr[8]+","  + arr[9] + "]")
print("[" + arr[10]+","  + arr[11]+","  + arr[12] +"," + arr[13] +"," + arr[14] + "]")
print("[" + arr[15]+","  + arr[16] +"," + arr[17]+","  + arr[18]+","  + arr[19] + "]")
print("[" + arr[20]+"," + arr[21]+"," + arr[22]+"," + arr[23] +","+ arr[24] + "]")