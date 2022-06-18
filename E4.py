entrada = input("Insira numero a verificar")
numero = float(entrada)
inteiro = int(numero)
if inteiro%5==0 and inteiro%3==0:
    print("FizzBuzz")
else:
    print(entrada)