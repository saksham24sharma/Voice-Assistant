import operator


key = int(input("Enter Key : "))
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
key_arr =[]
plain_arr = []
cipher_arr = []
de_cipher_arr=[]
de_key=[]
de_ci_ans = []

plain = input("Enter plain text : ")
cipher = input("Enter cipher text : ")

for p in plain:
    plain_arr.append(alpha.index(p))

key_arr.insert(1,operator.add(plain_arr[0],key))

for i in range(0,len(plain_arr)-1):
    key_arr.append(plain_arr[i])

cipher_arr.append(key_arr[0]%26)

for c in range(1,len(plain_arr)):
    cipher_arr.append((plain_arr[c] + key_arr[c])%26)

for ci_text in cipher_arr:
    print(alpha[ci_text],end="")

print("")

#De-cipher


for c in cipher:
    de_cipher_arr.append(alpha.index(c))

de_ci_ans.append((de_cipher_arr[0] - key))

for i in range(1,len(cipher)+1):
    de_ci_ans.append(de_cipher_arr[i] - de_ci_ans[i-1])

print(de_cipher_arr)