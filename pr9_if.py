a1a=int(input("Introduceti numarul bilelor albe mici a1a="))
b1a=int(input("Introduceti numarul bilelor albe mari b1a="))
a1r=int(input("Introducetinumarul bilelor rosii mici a1r="))
b1r=int(input("Introduceti numarul bilelor rosii mari b1r="))
a1v=int(input("Introduceti numarul bilelor verzi mici a1v="))
b1v=int(input("Intoduceti numarul bilelor verzi mari b1v="))
mari=b1a+b1r+b1v
mici=a1a+a1r+a1v
if mari>mici :
    print("sunt",mari,"bile mari")
else :
    print("sunt",mici,"bile mici")
a=a1a+b1a
r=a1r+b1r
v=a1v+b1v
if((a>r)and(a>v)):
    print(a)
if((r>a)and(r>v)):
    print(r)
if((v>a)and(v>r)):
    print(v)
