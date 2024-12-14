
velocidade = float(input("Digite a velocidade do carro (km/h): "))
if velocidade > 80:
    excesso = velocidade - 80
    multa = excesso * 20
    print(f"Você foi multado! O valor da multa é R${multa}.")
else:
    print("Você está dentro do limite de velocidade.")