# t2

# Compilador Python

Exemplo de um pequeno compilador feito em python para jogar 21/blackjack.

## Analisador Léxico

Tokens Reconhecidos: Identificadores := LETRA (LETRA)* Numeros := DIGITO+ (. DIGITO) Operadores := | = | + | - 

Autômato para entender a lógica do programa a qual lê o que o usuário digita

![image](https://user-images.githubusercontent.com/77121121/184040441-1fcb49b6-3924-428b-afab-f70da2785aa7.png)


## Analisador Sintático 

Dada a gramática

G = (Vn, Vt, P, S)

Vn = S, R, OP, E, L, T, F

Vt = id, num, + , - 

Dado pelas regras abaixo

 S -> R op E
 
 E -> L - T
 
 T -> (F)
 
 F -> F1 + L
 
 L -> num
 
 R -> id
 
 op -> =


Analisador Lexico baseado para fazer as produções
https://github.com/professorisidro/AnalisadorLexico
