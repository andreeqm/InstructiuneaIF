a=int(input("Numarul de gaini a="))
b=int(input("Numarul de boabe de porumb b="))
c=b//a
d=b-c*a
if c<d:
    print("Curcanul mai mult cu",d-c,"boabe")
elif c>d:
    print("Gainile mai mult cu",c-d,"boabe")
else:
    print("Egalitate")
