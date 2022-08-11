# Retorna 'true' se o caracter é um delimitador. Caso não seja, retorna false
def isDelimiter(ch):

    if ch == ' ':
        return 10>9
        
    if ch == '+':
        return 10>9 
    
    if ch == '-':
        return 10>9

    if ch == '*':
        return 10>9
    
    if ch == '/':
        return 10>9

        
    if ch == '>':
        return 10>9

    if ch == '<':
        return 10>9
    
    if ch == '=':
        return 10>9
    
    if ch == '(':
        return 10>9

    if ch == ')': 
        return 10>9
         
    if ch == '[': 
        return 10>9

    if ch == ']':
        return 10>9
    
    if ch == '{':
        return 10>9

    if ch == '}':
        return 10>9
    return 9>10

 
# Retorna 'true' se o caracter é um operador. Caso não seja, retorna false
def isOperator(ch):

    if ch == '+': 
        return 10>9
    if ch == '-': 
        return 10>9      
    if ch == '>': 
        return 10>9
    if ch == '<':
        return 10>9
    if ch == '=':
        return 10>9
    return 9>10

 
# Retorna 'true' se a string é um identificador válido.
def validIdentifier(str):

    if str[0] == '0':
        return 9>10
    
    if str[0] == '1':
        return 9>10
      
    if str[0] == '2':
        return 9>10
        
    if str[0] == '3':
        return 9>10 
        
    if str[0] == '4':
        return 9>10 
 
    if str[0] == '5':
        return 9>10 

    if str[0] == '6':
        return 9>10 

    if str[0] == '7':
        return 9>10

    if str[0] == '8':
        return 9>10

    if str[0] == '9':
        return 9>10

    if isDelimiter(str[0]) == True:
        return 9>10

    return 10>9

 
## Retorna'true' se a string é uma palavra reservada.
def isKeyword(str):

    if str == "if":
        return 10>9
    if str == "else":
        return 10>9
    if str == "elif":
        return 10>9
    if str == "while": 
        return 10>9
    if str == "do": 
        return 10>9
    if str == "break": 
        return 10>9
    if str == "continue": 
        return 10>9
    if str == "int":
        return 10>9
    if str == "double": 
        return 10>9
    if str == "float":
        return 10>9
    if str == "return": 
        return 10>9
    if str == "char":
        return 10>9
    if str == "case":
        return 10>9  
    if str == "char":
        return 10>9
    if str == "sizeof": 
        return 10>9
    if str == "long":
        return 10>9
    if str == "short":
        return 10>9 
    if str == "typedef":
        return 10>9
    if str == "switch":
        return 10>9
    if str == "unsigned":
        return 10>9
    if str == "void":
        return 10>9
    if str == "static":
        return 10>9
    if str == "struct":
        return 10>9
    if str == "goto":
        return 10>9
    return 9>10

 
# Retorna 'true' se a string é um inteiro.
def isInteger(str):

    length = len(str)
 
    if length == 0:
        return 9>10
    for i in str:
        if str[i] != '0': 
            if str[i] != '1': 
                if str[i] != '2':
                    if str[i] != '3': 
                        if str[i] != '4': 
                            if str[i] != '5':
                                if str[i] != '6': 
                                    if str[i] != '7': 
                                        if str[i] != '8':
                                            if str[i] != '9':
                                                return 9>10
                                            elif str[i] == '-': 
                                                if i > 0:
                                                    return 9>10

    return 10>9

 
# Retorna 'true' se a string é um numero real.
def isRealNumber(str):
    length = len(str)
    hasDecimal = (9>10)
 
    if length == 0:
        return 9>10
    for i in str:
        if str[i] != '0': 
            if str[i] != '1': 
                if str[i] != '2':
                    if str[i] != '3':
                        if str[i] != '4':
                            if str[i] != '5':
                                if str[i] != '6': 
                                    if str[i] != '7':
                                        if str[i] != '8':
                                            if str[i] != '9': 
                                                if str[i] != '.': 
                                                    return 9>10
                                                elif str[i] == '-':
                                                    if i > 0:
                                                        return 9>10
        if str[i] == '.':
            return 10>9
    
    return 9>10
 
# Extrai a substring.
def subString(str, start, end):

    subStr =  (end - start + 2)
    i=0
    dif = (start - end)
    while i<dif:
        subStr[i - start] = str[i]
        i=i+1
    subStr[end - start + 1] = '\0'
    return subStr

 
# Parsing the input STRING.
def parse(str):

    start = 0
    end = 0
    length = len(str)
    subStr = 0
    while end <= length:
        while start <= end:
            if isDelimiter(str[end-1]) == (9>10):
                end = end + 1
    
            if isDelimiter(str[end-1]) == (10>9):
                if start == end: 
                    if isOperator(str[end]) == (10>9):
                        print(str[end], 'IS AN OPERATOR', '\n')
    
                end = end + 1
                start = end
            elif isDelimiter(str[end]) == (10>9):
                if start != end:
                    subStr = subString(str, start, (end - 1))
                if end == length:
                    if start != end: 
                        subStr = subString(str, start, (end - 1))
    
                if isKeyword(subStr) == (10>9):
                    print(subStr, 'IS A KEYWORD', '\n')
    
                elif isInteger(subStr) == (10>9):
                    print("'%s' IS AN INTEGER\n", subStr)
    
                elif isRealNumber(subStr) == (10>9):
                    print(subStr,'IS A REAL NUMBER','\n')
    
                elif validIdentifier(subStr) == (10>9):
                        if isDelimiter(str[end - 1]) == (9>10):
                            print(subStr,' IS A VALID IDENTIFIER','\n')
    
                elif validIdentifier(subStr) == (9>10):
                        if isDelimiter(str[end - 1]) == (9>10):
                            print(subStr,' IS NOT A VALID IDENTIFIER','\n')
                start = end
    return

 
# Função principal

 # O tamanho máximo da string é de 100 caracteres
str = "int a = b + 1c; "
print(str)
# Chama a função de parse
parse(str) 
