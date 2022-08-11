#Somando dois números SEM E COM OO

Primeiro = int(input("Digite o primeiro número: "))
Segundo = int(input("Digite o segundo número: "))

resultado = Primeiro + Segundo
print("O resultado da soma entre {} e {} é {}".format(Primeiro, Segundo, resultado))



#Em OO podendo ser float ou int
def converte_numero(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError:
        try:
            valor = float(valor)
            return(valor)
        except ValueError:
            pass

Primeiro = converte_numero(input("Digite o primeiro número: "))
Segundo = converte_numero(input("Digite o segundo número: "))

resultado = Primeiro + Segundo

print("O resultado da soma entre {} e {} é {}".format(Primeiro, Segundo, resultado))

