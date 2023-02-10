import random

def jogar():

    print("###############################")
    print("Bem vindo no jogo de Advinhação")
    print("###############################")

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000
    print(numero_secreto)

    print("Qual o nível de dificuldade ?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível :"))

    if (nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa: {} de {}".format(rodada, total_de_tentativas))
        chute_string = input("Digite um número entre 1 e 100: ")

        print("Você digitou " , chute_string)

        chute = int(chute_string)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue # Ele pula a interação atual e vai para proxima.

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(maior):
                print("Você errou ! Seu chute foi maior que o número secreto")
                if(rodada == total_de_tentativas):
                    print("O número secreto era {}. Você fez {}".format(numero_secreto, pontos))
            elif(menor):
                print("Você errou ! Seu chute foi menor que o número secreto")
                pontos_perdidos = abs(numero_secreto - chute)
                pontos = pontos - pontos_perdidos
                if(rodada == total_de_tentativas):
                    print("O número secreto era {}. Você fez {}".format(numero_secreto, pontos))
        


    print("Fim do Jogo")

if(__name__ == "__main__"):
    jogar()