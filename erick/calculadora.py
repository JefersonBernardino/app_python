# Aulas de variaveis.
valor1_str = input('digite o primeiro valor: ') # pegando valor digitado na entrada.
print("valor1: " + valor1_str) # imprime o valor que o usuario  digitou.
valor2_str = input('digite o segundo valor: ') # pegando valor digitado na entrada
print("valor2: " + valor2_str) # imprime o valor que o usuario  digitou

soma= valor1_str + valor2_str # soma os dois valores.
print("resultado da str: " + soma) # imprime a soma dos valores.

valor1_int = int(valor1_str) # transformando 'string' em numero inteiro. porque de forma matematica não da para soma 2 string. string = letras
valor2_int = int(valor2_str) # transformando 'string' em numero inteiro. porque de forma matematica não da para soma 2 string. string = letras
soma = valor1_int + valor2_int # somando dois números inteiros.
soma_str = str(soma) # Tranformar inteiro em string
print("resultado do int: " + soma_str) # imprime o resultado.

# LICAO DE CASA, SEPARAR A LINHA 18 E COMENTAR O QUE FOI FEITO
subtracao = valor1_int - valor2_int
print("resultado do int: " + str(subtracao))
