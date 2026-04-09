# Multiplicação de Matrizes - Análise de Complexidade

A multiplicação de matrizes considera duas matrizes quadradas de ordem n × n.

O método tradicional utiliza três laços de repetição aninhados.

Para cada elemento da matriz resultado:
- são realizadas n multiplicações e somas

Como existem n² elementos na matriz resultado, o custo total é:

T(n) = n² * n

Resultado:
T(n) = Θ(n³)

Conclusão:
A complexidade da multiplicação tradicional de matrizes é cúbica.