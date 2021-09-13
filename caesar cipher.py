text = input("Enter text : ")
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
K = int(input("Enter key : "))
choice = input("Enter 1 for Cipher and 2 Decipher :")


def incrypt(text):
    for P in text:
        code=(alpha.index(P)+K)%26
        print(alpha[code].upper(),end='')


def decrypt(text):
    for P in text:
        decode = (alpha.index(P)-K)%26
        print(alpha[decode].lower(),end='')


if (K < 0 or K> 25):
    print("Invalid key")
else:
    if (choice == "1"):
        if(text.islower()):
            incrypt(text)
        else:
            print("Enter in lower case")
    elif (choice == "2"):
        if(text.isupper()):
            text=text.lower()
            decrypt(text)
        else:
            print("Enter in upper case")
    else:
        print("Invalid choice")