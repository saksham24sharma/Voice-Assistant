command = input("Enter instruction: ")
started = False
while command.upper() != "EXIT":
    if command.upper() == "START":
        if started == True:
            print("GADDI PEHLE TO HE CHALU A")
        else:
            started = True
            print("GADDI CHALLU")
        command = input("Enter instruction: ")
    elif command.upper() == "STOP":
            if started == False:
                print("OYE GADDI PELHE TO HE RUKI AA")
            else:
                print("GADDI RUK GAYI")
                started = False
            command = input("Enter instruction: ")
    elif command.upper() == "HELP":
        print("COMMANDS ARE:")
        print("START")
        print("STOP")
        print("EXIT")
        command = input("Enter instruction: ")
    else:
        print("WRONG INSTRUCTION")
        command = input("Enter instruction: ")
else:
    print("TATA BYE BYE")