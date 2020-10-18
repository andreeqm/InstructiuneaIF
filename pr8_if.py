n1=int(input("Introduceti primul numar n1="))
n2=int(input("Introduceti al doilea numar n2="))
if((n1//2==0)and(n2//2==0)) :
    if(n1>n2) :
        print("n1")
    else :
        print("n2")
elif((n1//2==0)and(n2//2!=0)) :
    print("n1")
elif((n1//2!=0)and(n2//2==0)) :
    print("n2")
elif((n1//2!=0)and(n2//21!=0)) :
    print("nu exista numere pare")