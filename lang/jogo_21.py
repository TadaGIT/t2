import random

dealer_cartas = []

jogador_cartas = []

while len(dealer_cartas) != 2:
    dealer_cartas.append(random.randint(1, 11))
    if len(dealer_cartas) == 2:
        print("Dealer tem ", dealer_cartas)

if sum(dealer_cartas) == 21:
    print("o Dealer tem 21 e ganhou!")
elif sum(dealer_cartas) > 21:
    print("O Dealer parou!!")

while sum(jogador_cartas) < 21:
    acao_tomada = str(input("Voce quer parar, ou continuar?  "))
    if acao_tomada == "continuar":
        jogador_cartas.append(random.randint(1, 11))
        print("Voce agora tem um total de " + str(sum(jogador_cartas)) + "destas cartas ", jogador_cartas)
    else:
        print("O dealer tem um total de " + str(sum(dealer_cartas)) + "com " , dealer_cartas)
        print("Voce tem um total de " + str(sum(jogador_cartas)) + "com", jogador_cartas)
        if sum(dealer_cartas) > sum(jogador_cartas):
            print("Dealer ganhou!!!")
        else:
            print("Voce ganhou!!!") 
            break
if sum(jogador_cartas) > 21:
    print("Voce perdeu, o dealer ganhou!!")
elif sum(jogador_cartas) == 21:
    print("Voce ganhou!!! fez 21!!!")