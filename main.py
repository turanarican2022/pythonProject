# WHILE LOOPS

names = []
ask = True
while ask:
    inp=input("please write your name or type \"end\" : ")
    if inp != "end":
        names.append(inp)
    else:
        ask=False
print(names)
