import random


print("=-" * 17)
print("Bem vindo ao jogo da Adivinhação!")
print("-=" * 17)

numero_secreto = round(random.randrange(1,101))

total_de_tentativas = 3

for rodada in range(1, total_de_tentativas + 1):
    print(f"Rodada {rodada} de {total_de_tentativas}")

    chute = int(input("Digite um número entre 1 e 100: "))
    print(f"Você digitou: {chute}")

    if(chute < 1 or chute > 100):
        print("Digite um número entre 1 e 100!!")
        continue
    
    
    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Você acertou!!")
        break
    else:
        if(maior):
            print("Você errou, o chute foi maior que o número secreto!!")

        elif(menor):
            print("Você errou, o chute foi menor que o número secreto!!")

print("-*" * 17)
print("Fim do jogo!!") 

