n1=int(input("Introduceti primul numar n1="))
n2=int(input("Introduceti al doilea numar n2="))
n3=int(input("Introduceti al treilea numar n3="))
if((n1>0)and(n2>0)and(n3>0)) :
    if(n2>n3) :
        print("n2")
    if(n2<n3) :
        print("n3") 
else :
    print(n1+n2)    