a=int(input("Introduceti primul numar a="))
b=int(input("Introduceti al doilea numar b="))
c=int(input("Introduceti al treilea numar c="))
if(a<32000)and(b<32000)and(c<32000) :
    if((a<b+c)and(b<a+c)and(c<b+a)) :
        print("DA")
    else :
        print("NU")    