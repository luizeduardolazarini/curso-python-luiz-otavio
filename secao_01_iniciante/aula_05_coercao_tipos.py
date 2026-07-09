# Conversao de tipos em Python
# Coercao de tipos (type coercion) é o processo de converter um tipo de dado em outro tipo de dado. Em Python, isso pode ser feito de forma implícita ou explícita.
# Coercao implicita ocorre quando o interpretador do Python converte automaticamente um tipo de dado em outro tipo de dado, sem a necessidade de intervenção do programador. 
# Por exemplo, quando um número inteiro é somado a um número de ponto flutuante, o Python converte automaticamente o inteiro em ponto flutuante antes de realizar a operação.
print(10 + 5.5)  # 15.5, o inteiro 10 é convertido para ponto flutuante antes da soma
print(type(10 + 5.5))  # <class 'float'>
print(10 + True)  # 11, o booleano True é convertido para inteiro 1 antes da soma
print(type(10 + True))  # <class 'int'>
print(int("10") + 5)  # 15, a string "10" é convertida para inteiro antes da soma
print(str(10) + "5")  # "105", o inteiro 10 é convertido para string antes da concatenação
