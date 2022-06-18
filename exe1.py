import math
pontox1 = input("Insira coordenada x do ponto 1")
x1=float(pontox1)
pontoy1 = input("Insira coordenada y do ponto 1")
y1=float(pontox1)
pontox2 = input("Insira coordenada x do ponto 2")
x2=float(pontox2)
pontoy2 = input("Insira coordenada y do ponto 2")
y2=float(pontox2)
distancia=math.sqrt((x1-x2)**2+(y1-y2)**2)
if distancia<=10:
    print("perto")
else:
    print("longe")