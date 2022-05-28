
print("*-" * 17)
print("Bem vindo ao jogo da Adivinhação!")
print("-*" * 17)

numero_secreto = 42

chute = int(input("Digite o seu número: "))

print(f"Você digitou: {chute}")

acertou = numero_secreto == chute
maior = chute > numero_secreto
menor = chute < numero_secreto

if(acertou):
    print("Você acertou!!")
else:
    if(maior):
        print("Você errou, o chute foi maior que o número secreto!!")

    elif(menor):
        print("Você errou, o chute foi menor que o número secreto!!")

print("-*" * 17)
print("Fim do jogo!!") 

