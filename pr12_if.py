x=int(input("Numarul petalelor x="))
if x>0:
    print("Ma iubeste...")
    if x%6==0:
        print("...un pic")
    elif x%6==5:
        print("...mult")
    elif x%6==4:
        print("...cu pasiune")
    elif x%6==3:
        print("...la nebunie")
    elif x%6==2:
        print("...de loc")
    else:
        print("...un pic")
else:
    'break'