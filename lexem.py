import re

exp = input("Enter the expresion : ")
spt = re.split("[, =;]", exp)
keywords = ["auto", "break", "case", "char", "const", "continue", "default", "double", "enum", "extern", "float", "for",
            "goto", "if", "int", "long", "register", "return", "short", "signed",
            "sizeof", "static", "struct", "switch", "typeof", "union", "unsigned", "void", "volatile", "while", "do",
            "else"]

for key in spt:
    if key in keywords:
        print(key +" is keyword")


flag1 = False
flag2 = False
count = 0

for words in spt:
    if words not in keywords:

        if re.findall("^[a-zA-Z_]", words):
            flag1 = True

            #for i in spt:
            if re.search(r'[!@=#%$&]', words):
                flag2 = True
                    #count = count + 1

            #if count >= len(words):
             #   flag2 = True

            if flag1 == True and flag2 == False:
                print(words + " is a identifier")
