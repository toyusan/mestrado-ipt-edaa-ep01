# Multiplicação de números grandes

---

Tabela de conteúdos
=================
<!--ts-->
   * [Sobre o projeto](#-sobre-o-projeto)
   * [Funcionalidades](#-funcionalidades)
   * [Como executar o projeto](#-como-executar-o-projeto)
     * [Pré-requisitos](#pré-requisitos)
     * [Rodando o programa](#user-content--rodando-o-programa)
	 * [Exemplos de testes](#user-content--exemplos-de-testes)
   * [Autor](#-autor)
   * [Licença](#user-content--licença)
<!--te-->

---

## Sobre o projeto

Solução do Exercício Programa 01 da matéria Estrutura de Dados e Analise de Algoritmos do curso de Mestrado em Computação Aplicada do IPT, referente ao 3° Quadrimestre de 2021:

> "O algoritmo para multiplicação de dois valores inteiros X[1..n] e Y [1..n], de n
algarismos, que aprendemos na época do ensino fundamental, tem complexidade de
tempo Θ(n2). Porém, existe um método de divisão e conquista, conhecido como
algoritmo de Karatsuba, publicado em 1962, que realiza a mesma tarefa com complexidade
O(n^log3^) =~ O(n^1.58^). Implemente os algoritmos de multiplicação tradicional (do ensino fundamental) e
de Karatsuba (apresentado a seguir). Seu programa deve receber dois inteiros X[1..n]
e Y [1..n], devolver o produto X ·Y , e mostrar o tempo de execução dos 2 algoritmos.

>Karatsuba (X, Y , n):
>1. se (n ≤ 3) retorna X · Y
>2. q ← |n/2|
>3. A ← X[q + 1..n]; B ← X[1..q]
>4. C ← Y [q + 1..n]; D ← Y [1..q]
>5. E ← Karatsuba (A, C, |n/2|)
>6. F ← Karatsuba (B, D, |n/2|)
>7. G ← Karatsuba (A + B, C + D, |n/2| + 1)
>8. H ← G − F − E
>9. R ← E × 10^2*|n/2|^ + H × 10^1*|n/2|^ + F
>10. retorna R"

---

## Funcionalidades

- O usuário entra com dois valores inteiros X e Y, de n algarismos;
- O software calcula o resultado da multiplicação dos números X e Y usando os algoritimos do ensino fundamental e de Karatsuba;
- O software apresenta o tempo de execução dos dois algoritmos, em nano segundos; 
---

## Como executar o projeto

### Pré-requisitos

* [Python 3.8.7](https://www.python.org/downloads/release/python-387/);
 
#### Rodando o programa

- Localizar o arquivo ep01.py e clicar duas vezes para abri-lo;

#### Exemplos de testes

#### Primeiro exemplo

> X = 654896548922222

> Y = 222226548922222

> Resultado da multiplicacao tradicional: 145535399968058520689805417284 e levou 560646 nanosegundos

> Resultado da multiplicacao karatsuba:   145535399968058520689805417284 e levou 4643 nanosegundos

#### Segundo exemplo

> X = 123456789123456789123456789123456789123456789123456789

> Y = 123456789123456789123456789123456789123456789123456789

> Resultado da multiplicacao tradicional: 15241578780673678546105778311537878076969977842402077577351019811918920046486820281054720515622620750190521 e levou 2333147 nanosegundos

> Resultado da multiplicacao karatsuba:   15241578780673678546105778311537878076969977842402077577351019811918920046486820281054720515622620750190521 e levou 4927 nanosegundos
 
#### Terceiro exemplo

> X = 987654321987654321987654321987654321987654321987654321987654321987654321987654321987654321987654321987654321

> Y = 987654321987654321987654321987654321987654321987654321987654321987654321987654321987654321987654321987654321

> Resultado da multiplicacao tradicional: 975461059740893159506325259271757359037189458802621558568053658333485758098917857864349957629782057395214155209724137444292037678859937913427838147995738382563638617131538851699439086267339320835239555403139789971041 e levou 12173215 nanosegundos

> Resultado da multiplicacao karatsuba:   975461059740893159506325259271757359037189458802621558568053658333485758098917857864349957629782057395214155209724137444292037678859937913427838147995738382563638617131538851699439086267339320835239555403139789971041 e levou 8719 nanosegundos

---

### Autor 

- Airton Y. C. Toyofuku
- airton.toyofuku@gmail.com

---
### Licença
Este projeto esta sob a licença [MIT](./LICENSE).
