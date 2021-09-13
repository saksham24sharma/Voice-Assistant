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


explist = re.split('[\W]+',exp)
seplist = list(exp)
no = ["1","2","3","4","5","6","7","8","9","0"]
operators = ["+","-","/","*","<",">","%","=","==","<=",">="]
seperators = [";",",",".","(",")","[","]","{","}"]
operator = re.split('[\w]+',exp)

for k in explist:
    if k in re.findall('[0-9]+',k):
        print(k + " is a number")

for oprt in operator:
    if oprt in operators:
        print(oprt + " is an operator")

for s in seplist:
    if s in seperators:
        print(s + " is seperator")