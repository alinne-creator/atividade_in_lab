a = int(input("digite o primeiro numero: "))
b = int(input("digite o segundo numero: "))

if(a < b):
    soma = 0
    for termo in range(a,b+1):
        soma=soma+termo
    print(soma)
elif (a > b):
    print("Error, tente novamente.")
