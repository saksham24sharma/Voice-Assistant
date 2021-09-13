command = input(">")
cmdd = command.split(" ")
emoji = {
    ":)" : "😊",
    ":(" : "😒"
}
output = ""
for word in cmdd:
    output= output + emoji.get(word,word) + " "
print(output)