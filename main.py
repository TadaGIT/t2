import json
import random

## Definições regulares 
# id : [a-z]
# num : [0-9]

## Tokens: 
# "+", 
# "-", 
# "=", 
# "abs", 
# "(",
# ")", 
# "NAME"
# "R"
# "E"
# "L"
# "T"
# "F"
# "parar"
# "continuar"

## Regras
#   S -> R = E
#   E -> L - T
#   T -> (F)
#   F -> F1 + L
#   L -> num
#   R -> id

## Expressões regulares
# [0-9] + [a-z] 

with open("cartas.json", encoding='utf-8') as baralho:
    dados = json.load(baralho)



for i in dados:
    print('Cartas do baralho: /n --------------- /n', i['numero'], ' de ', i['tipo'], '/n --------------- /n')





dealer_cartas = []

jogador_cartas = []
while sum(dealer_cartas) < 17:
    dealer_cartas.append(random.randint(2, 11))
        
print("Dealer tem ", dealer_cartas)       

if sum(dealer_cartas) == 21:
    print("o Dealer tem 21 e ganhou!")
elif sum(dealer_cartas) > 21:
    print("O Dealer parou!!")

while sum(jogador_cartas) < 21:
    acao_tomada = str(input("Voce quer parar, ou continuar?  "))
    if acao_tomada == "continuar":
        jogador_cartas.append(random.randint(2, 11))
        print("Voce agora tem um total de " + str(sum(jogador_cartas)) + " destas cartas ", jogador_cartas)
    else:
        print("O dealer tem um total de " + str(sum(dealer_cartas)) + " com " , dealer_cartas)
        print("Voce tem um total de " + str(sum(jogador_cartas)) + " com", jogador_cartas)
        if sum(dealer_cartas) > 21:
                print("Dealer estorou!!! Você ganhou!!!")
                break
        if sum(dealer_cartas) > sum(jogador_cartas):
            
            print("Dealer ganhou!!!")
        else:
            print("Voce ganhou!!!") 
            break
if sum(jogador_cartas) > 21:
    print("Voce perdeu, o dealer ganhou!!")
elif sum(jogador_cartas) == 21:
    print("Voce ganhou!!! fez 21!!!")

 