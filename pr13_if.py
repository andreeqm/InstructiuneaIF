x=int(input("Introduceti locul x="))
if (x>=1) and (x<25):
    print("Alba")
elif(x>=25) and (x<50):
    print("Rosie")
elif(x>=50) and (x<75):
    print("Albastra")
elif(x>=75) and (x<=100):
    print("Neagra")
elif x>100:
    print("Nu a primit tricou")
else:
    'break'