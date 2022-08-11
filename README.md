![image](https://user-images.githubusercontent.com/77121121/184261474-f20ef41d-7711-40c6-bbe4-68a3b7b746d4.png)

# Compilador Python

Exemplo de um pequeno compilador feito em python para jogar 21/blackjack.

## Analisador Léxico

Tokens Reconhecidos: Identificadores := LETRA (LETRA)* Numeros := DIGITO+ (. DIGITO) Operadores := | = | + | - 

Palavras reservadas := continuar, parar

Autômato para entender a lógica do programa a qual lê o que o usuário digita

![image](https://user-images.githubusercontent.com/77121121/184040441-1fcb49b6-3924-428b-afab-f70da2785aa7.png)


## Analisador Sintático 

Dada a gramática 

G = (Vn, Vt, P, S)

Vn = S, R, op, E, L, T, F

Vt = id, num, + , - 

Dado pelas regras abaixo  ----------- | -----------     Regra semântica

 S -> R op E  -----------------------  resultado := abs(expr)
  
 E -> L - T    ----------------------- expr := 21 - sum             
 
 T -> (F)      ----------------------- sum := "("||F.val||")"        
 
 F -> F1 + L    ----------------------- F := F1.val + L.val       
 
 L -> num     ----------------------- L := num.val                   # num.val é carregado de cartas.json
 
 R -> id      ----------------------- R := id.cod
 
 op -> =       ----------------------- op := =


Analisador Lexico baseado para fazer as produções
https://github.com/professorisidro/AnalisadorLexico

Para criar o analisador Lexico, foi utilizado como base o regex em c
https://thobias.org/doc/er_c.html
