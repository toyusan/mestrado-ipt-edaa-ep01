# Multiplicação de números grandes

---

Tabela de conteúdos
=================
<!--ts-->
   * [Sobre o projeto](#user-content--sobre-o-projeto)
   * [Funcionalidades](#user-content--funcionalidades)
   * [Como executar o projeto](#user-content--como-executar-o-projeto)
     * [Pré-requisitos](#user-content-pré-requisitos)
     * [Rodando o programa](#user-content--rodando-o-programa)
	 * [Exemplos de testes](#user-content--exemplos-de-testes)
   * [Autor](#user-content--autor)
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

> Karatsuba (X, Y , n):
> 1. se (n ≤ 3) retorna X · Y
> 2. q ← teto(n/2)
> 3. A ← X[q + 1..n]; B ← X[1..q]
> 4. C ← Y [q + 1..n]; D ← Y [1..q]
> 5. E ← Karatsuba (A, C, teto(n/2))
> 6. F ← Karatsuba (B, D, piso(n/2))
> 7. G ← Karatsuba (A + B, C + D, teto(n/2) + 1)
> 8. H ← G − F − E
> 9. R ← E × 10^(2*teto(n/2)) + H × 10^teto(n/2) + F
> 10. retorna R"

O algoritmo descrito no enunciado do problema parece ter alguns erros, por isso o autor tomou a liberdade de fazer alguns ajustes:

>1. O parametro E foi trocado com o parametro F na linha 9;
>2. A soma de A+B e C+D podem gerar um numeros de tamanhos diferentes, por isso o tamanho foi igualado com 0 a esquerda;
>3. O parametro |n/2| + 1 foi substituido pelo tamanho do vetor gerado pela soma A+B ou C+D, já igualados;
---

## Funcionalidades

- O usuário entra com dois valores inteiros X e Y, de n algarismos;
- O software calcula o resultado da multiplicação dos números X e Y usando os algoritimos do ensino fundamental e de Karatsuba;
- O software apresenta o tempo de execução dos dois algoritmos, em segundos; 
---

## Como executar o projeto

### Pré-requisitos

* [Python 3.8.7](https://www.python.org/downloads/release/python-387/);
 
#### Rodando o programa

- Localizar o arquivo ep01.py e clicar duas vezes para abri-lo;

#### Exemplos de testes

#### Primeiro exemplo

> Entre com o valor de X: 654896548922222

> Entre com o valor de Y: 222226548922222

> Resultado da multiplicacao tradicional: 145535399968058520689805417284 e levou 0.00021309999999985507 segundos

> Resultado da multiplicacao karatsuba:   145535399968058520689805417284 e levou 0.00023109999999881836 segundos


#### Segundo exemplo

> Entre com o valor de X: 123456789123456789123456789123456789123456789123456789

> Entre com o valor de Y: 123456789123456789123456789123456789123456789123456789

> Resultado da multiplicacao tradicional: 15241578780673678546105778311537878076969977842402077577351019811918920046486820281054720515622620750190521 e levou 0.002128299999999861 segundos

> Resultado da multiplicacao karatsuba:   15241578780673678546105778311537878076969977842402077577351019811918920046486820281054720515622620750190521 e levou 0.0006614000000002562 segundos
 
#### Terceiro exemplo

> Entre com o valor de X: 987654321987654321987654321987654321987654321987654321987654321987654321987654321987654321987654321987654321

> Entre com o valor de Y: 987654321987654321987654321987654321987654321987654321987654321987654321987654321987654321987654321987654321

> Resultado da multiplicacao tradicional: 975461059740893159506325259271757359037189458802621558568053658333485758098917857864349957629782057395214155209724137444292037678859937913427838147995738382563638617131538851699439086267339320835239555403139789971041 e levou 0.008858500000000546 segundos

> Resultado da multiplicacao karatsuba:   975461059740893159506325259271757359037189458802621558568053658333485758098917857864349957629782057395214155209724137444292037678859937913427838147995738382563638617131538851699439086267339320835239555403139789971041 e levou 0.0014525000000000787 segundos

---

### Autor 

- Airton Y. C. Toyofuku
- airton.toyofuku@gmail.com

---
### Licença
Este projeto esta sob a licença [MIT](./LICENSE).
