
print("*-" * 17)
print("Bem vindo ao jogo da Adivinhação!")
print("-*" * 17)

numero_secreto = 42

chute = int(input("Digite o seu número: "))

print(f"Você digitou: {chute}")

if(numero_secreto == chute):
    print("Você acertou!!")
else:
    if(chute > numero_secreto):
        print("Você errou, o chute foi maior que o número secreto!!")
        
    if(chute < numero_secreto):
        print("Você errou, o chute foi menor que o número secreto!!")



    print("Você errou!!")

print("-*" * 17)
print("Fim do jogo!!") 

