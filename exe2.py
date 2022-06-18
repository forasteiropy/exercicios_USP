import math
a=input("Insira componente A da equação de segundo grau")
aa=float(a)
b=input("Insira componente B da equação de segundo grau")
bb=float(b)
c=input("Insira componente C da equação de segundo grau")
cc=float(c)
delta =(bb**2)-4*aa*cc
if delta<0:
    print("esta equação não possui raízes reais")
else:
    if delta==0:
        raiz1=(-bb+math.sqrt(delta))/(2*aa)
        print("a raiz desta equação é",raiz1)
    else:
        raiz1=(-bb+math.sqrt(delta))/(2*aa)
        raiz2=(-bb-math.sqrt(delta))/(2*aa)
        if raiz1>raiz2:
            print("as raízes da equação são",raiz1,"e",raiz2)
        else:
            print("as raízes da equação são",raiz2,"e",raiz1)