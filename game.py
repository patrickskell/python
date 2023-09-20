import random

def play_game():
    num = random.randint(1, 100)
    tentativas = 0

    print("Bem vindo ao jogo de advinhação!")
    print("Fale um número de 1 a 100")

    while True:
        adv = int(input("Número: "))
        tentativas += 1

        if adv < num:
            print("Baixo demais.")
        elif adv > num:
            print("Alto demais.")
        else:
            print("Acertou em", tentativas, "tentativas.")
            break

    jogar_denovo = input("Quer jogar denovo? (s/n): ")
    if jogar_denovo.lower() == "s":
        play_game()
    else:
        print("Valeu!")

play_game()
