try:
    N = int(input("Enter no. of insertion :"))
except ValueError:
    print("ValueError")
else:
    numb = []
    i = 0
    while i != N:
        command = input("command ")
        if command == "insert":
            inx = int(input("Enter index value"))
            no = int(input("Enter no. to be inserted"))
            numb.insert(inx, no)
            print(numb)
        elif command == "append":
            no = int(input("Enter no. to be inserted"))
            numb.append(no)
            print(numb)
        elif command == "print":
            print(numb)
        elif command == "remove":
            no = int(input())
            numb.remove(no)
            print(numb)
        elif command == "pop":
            if numb.__len__() != 0:
                numb.pop()
            else:
                print(numb)
        elif command == "sort":
            numb.sort()
            print(numb)
        elif command == "reverse":
            numb.reverse()
            print(numb)
        i = i+1
    else:
        print("Invalid command")