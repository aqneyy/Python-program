s=input("Enter a string: ")
len_s = len(s)
if len_s > 2:
    if s[-3:] == "ing":
        print(s + "ly")
    else:
        print(s + "ing")
else:
    print(s)
