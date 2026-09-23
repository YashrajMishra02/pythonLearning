# Program to greet all the person names stored in list "l" and which starts with s

l = ("Samay","Yashraj","Chetna","akash","Sonali","Rita","Shailesh")
for i in range(len(l)): # for name in l:
    if("S" in l[i]): # if(name.startswith("S"))
        print("Your Welcome:", l[i])
