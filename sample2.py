name = input("Enter name: ")
alphabet = input("Enter an alphabet: ")
inxd = int(input("Enter index : "))
new_name = list(name)
new_name.insert(inxd,alphabet)
n =""
for i in new_name:
    n = n +i
print(n)