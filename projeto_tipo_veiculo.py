rodas = int(input("Digite a quantidade de rodas do veículo: "))
peso = float(input("Digite o peso bruto (Kg): "))
pessoas = int(input("Digite a quantidade de pessoas: "))

#Categoria A
if rodas == 2 or rodas == 3:
    categoria = 'A'
#Categoria B
elif rodas == 4 and pessoas <= 8 and peso <= 3500:
    categoria = 'B'
#Categoria C
elif rodas >= 4: 
    if peso > 3500 and peso < 6000:
        categoria = 'C'
#Categoria D
    if pessoas > 8:
        categoria = 'D'
#Categoria E
    if peso > 6000:
        categoria = 'E'
print("A melhor categoria de habilitação para o veiculo informado é: ",categoria)