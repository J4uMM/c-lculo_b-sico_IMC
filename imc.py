def main():
    peso = float(input("Digite seu peso em kg: "))
    altura = float(input("Digite sua altura em metros: "))
    imc = calculo_imc(peso, altura)
    print(f"Seu IMC é: {imc:.2f}")
    print(f"Categoria de peso: {classificar_imc(imc)}")

def calculo_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Pesoa normal"
    elif 24.9 <= imc < 29.9:
        return "Sobrepeso"
    elif 29.9 <= imc < 34.9:
        return "Obesidade 1"
    elif 34.9 <= imc < 39.9:
        return "Obesidade 2"
    else:
        return "Obesidade 3"


main()

    