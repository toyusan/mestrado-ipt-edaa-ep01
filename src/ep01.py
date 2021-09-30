########################################################################################################################
# @file     ep01.py
# @author   Airton Yassushiko Coppini Toyofuku
# @date     15/09/2021
# @brief    Solução do Exercício Programa 01 da matéria Estrutura de Dados e Analise de Algoritmos do curso de Mestrado
#           em Computação Aplicada do IPT, referente ao 3° Quadrimestre de 2021:
########################################################################################################################

########################################################################################################################
# "O algoritmo para multiplicação de dois valores inteiros X[1..n] e Y [1..n], de n
# algarismos, que aprendemos na época do ensino fundamental, tem complexidade de
# tempo Θ(n2). Porém, existe um método de divisão e conquista, conhecido como
# algoritmo de Karatsuba, publicado em 1962, que realiza a mesma tarefa com complexidade
# O(n^log3) =~ O(n^1.58). Implemente os algoritmos de multiplicação tradicional (do ensino fundamental) e
# de Karatsuba (apresentado a seguir). Seu programa deve receber dois inteiros X[1..n]
# e Y [1..n], devolver o produto X ·Y , e mostrar o tempo de execução dos 2 algoritmos.
#
# >Karatsuba (X, Y , n):
# >1. se (n ≤ 3) retorna X · Y
# >2. q ← (n/2)
# >3. A ← X[q + 1..n]; B ← X[1..q]
# >4. C ← Y [q + 1..n]; D ← Y [1..q]
# >5. E ← Karatsuba (A, C, n/2)
# >6. F ← Karatsuba (B, D, n/2)
# >7. G ← Karatsuba (A + B, C + D, n/2 + 1)
# >8. H ← G − F − E
# >9. R ← E × 10^(2*(n/2)) + H × 10^(n/2) + F
# >10. retorna R"
########################################################################################################################

########################################################################################################################
#  @brief  efetua a multiplicação de dois numeros naturais pelo algoritmo tradicional
#  @param  X: vetor com o primeiro numero natural
#  @param  Y: vetor com o segundo numero natural
#  @param  n: quantidade de algarismos
#  @retval valor da multiplicacao de X*Y
def multiplicacao_tradicional (X, Y, n):

    somatorio = 0

    # Multiplicando item a item do vetor
    for i in range (n-1, -1, -1):
        soma_parcial = ''
        carry = 0
        for j in range(n-1, -1, -1):
            Z = int(X[i]) * int(Y[j]) + carry

            #Checando se a multiplicaçao gerou um numero de dois algarismos
            if(Z > 9):
                carry = Z//10
            else:
                carry = 0

            Z = str(Z)
            soma_parcial = Z[len(Z)-1] + soma_parcial

        # Checando se ainda falta "apendar" um algarismo
        if(carry > 0):
            soma_parcial = str(carry) + soma_parcial

        # Realizando as somatorias parciais e multiplicando pela casa (dezena, centena, milhar...etc)
        somatorio = somatorio + int(soma_parcial) * 10**(n-i-1)

    return somatorio

########################################################################################################################
#  @brief  efetua a multiplicação de dois numeros naturais pelo algoritmo de karatsuba
#  @param  X: vetor com o primeiro numero natural
#  @param  Y: vetor com o segundo numero natural
#  @param  n: quantidade de algarismos
#  @retval valor da multiplicacao de X*Y
def multiplicacao_karatsuba (X, Y, n):

    import math

    if(n >= 3):
        return int(X) * int(Y)

    q = math.ceil(n/2)

    A = X[q:n]
    B = X[0:q]
    C = Y[q:n]
    D = Y[0:n]

    E = multiplicacao_karatsuba(A, C, math.floor(n/2))
    F = multiplicacao_karatsuba(B, D, math.ceil(n/2))
    G = multiplicacao_karatsuba( str(int(A) + int(B)), str(int(C) + int(D)), math.ceil(n/2) + 1)
    H = G - F - E
    R = E * 10**(2*math.ceil(n/2)) + H * 10**(math.ceil(n/2)) + F

    return R

########################################################################################################################

print("============================================")
print("=    Multiplicacao de numeros grandes      =")
print("============================================")

import time

#X = input("> Entre com o valor de X: ")
#Y = input("> Entre com o valor de Y: ")

X = "123456789123456789123456789123456789123456789123456789"
Y = "123456789123456789123456789123456789123456789123456789"

# Deixando os dois numeros com a mesma quantidade de algarismos
if(len(X) > len(Y)):
    Y.zfill(len(X))
if (len(Y) > len(X)):
    X.zfill(len(Y))

n = max(len(X), len(Y))

# Iniciando a multiplicacao via algoritmo tradicional
start_tradicional = time.time_ns()
resultado_tradicional = multiplicacao_tradicional(X, Y, n)
end_tradicional = time.time_ns()

tempo_tradicional = end_tradicional - start_tradicional

print("> Resultado da multiplicacao tradicional:", resultado_tradicional, "e levou", tempo_tradicional, "nanosegundos")

# Iniciando a multiplicacao via algortimo de karatsuba
start_karatsuba = time.time_ns()
resultado_karatsuba = multiplicacao_karatsuba(X, Y, n)
end_karatsuba = time.time_ns()

tempo_karatsuba = end_karatsuba - start_karatsuba

print("> Resultado da multiplicacao karatsuba:  ", resultado_karatsuba, "e levou", tempo_karatsuba, "nanosegundos")

print("============================================")

saida = input("> Precione qualquer tecla para sair...")