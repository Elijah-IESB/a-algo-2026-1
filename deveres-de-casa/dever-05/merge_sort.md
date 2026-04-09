# Merge Sort - Análise de Complexidade

O Merge Sort é um algoritmo de ordenação baseado na técnica de divisão e conquista.

Ele divide o vetor em duas partes iguais, ordena cada parte recursivamente e,
em seguida, realiza a junção (merge) das partes ordenadas.

A recorrência que descreve o algoritmo é:

T(n) = 2T(n/2) + n

Onde:
- 2T(n/2): duas chamadas recursivas
- n: custo da intercalação (merge)

Aplicando o Teorema Mestre:
- a = 2
- b = 2
- f(n) = n

Cálculo:
n^(log_b a) = n^(log₂2) = n

Comparação:
f(n) = Θ(n) = Θ(n^(log_b a))

Caso:
Caso 2 do Teorema Mestre

Resultado final:
T(n) = Θ(n log n)