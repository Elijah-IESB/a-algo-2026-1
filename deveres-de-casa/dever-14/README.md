# Dever 14 — Redução de Ciclo Hamiltoniano para Caixeiro Viajante

**Grupo 7**

## Objetivo

A empresa já possui um software que resolve exatamente o Problema do Caixeiro
Viajante (PCV), mas agora precisa decidir se um grafo possui um Ciclo
Hamiltoniano. Para reutilizar o software existente, mostraremos a redução
polinomial:

$$
\text{Ciclo Hamiltoniano} \leq_p \text{Caixeiro Viajante}.
$$

## Construção da redução

Considere uma instância do problema do Ciclo Hamiltoniano formada por um grafo
não direcionado $G=(V,E)$, com $n=|V|$ vértices.

Construímos uma instância do PCV da seguinte maneira:

1. Criamos um grafo completo $G'=(V,E')$ com os mesmos vértices de $G$.
2. Para cada par de vértices $u,v$, definimos o custo da aresta como:

   $$
   c(u,v)=
   \begin{cases}
   1, & \text{se } (u,v)\in E;\\
   2, & \text{se } (u,v)\notin E.
   \end{cases}
   $$

3. Executamos o software do Caixeiro Viajante em $G'$ para obter o custo
   mínimo de uma rota que visite todos os vértices uma vez e retorne ao ponto
   inicial.
4. Respondemos **sim** para o Ciclo Hamiltoniano se, e somente se, o custo
   mínimo encontrado for menor ou igual a $n$.

Como toda rota do PCV usa exatamente $n$ arestas e cada aresta custa pelo
menos 1, o custo nunca pode ser menor que $n$. Portanto, o teste também pode
ser escrito como "custo mínimo igual a $n$".

## Prova de correção

### Se G possui um Ciclo Hamiltoniano, então o PCV possui uma rota de custo n

Um Ciclo Hamiltoniano de $G$ visita todos os $n$ vértices exatamente uma
vez e retorna ao vértice inicial. Todas as suas arestas pertencem a $E$, logo
recebem custo 1 em $G'$. Como o ciclo usa $n$ arestas, seu custo total é
$n$. Assim, o software do PCV encontrará uma solução de custo no máximo $n$.

### Se o PCV possui uma rota de custo no máximo n, então G possui um Ciclo Hamiltoniano

Uma rota do PCV em $G'$ usa exatamente $n$ arestas. Para que seu custo seja no
máximo $n$, todas elas precisam ter custo 1. Pela construção, uma aresta
tem custo 1 somente quando pertence ao conjunto $E$ do grafo original.
Portanto, a rota encontrada usa apenas arestas de $G$, visita todos os
vértices uma vez e retorna à origem. Ela é, assim, um Ciclo Hamiltoniano de
$G$.

Logo:

$$
G \text{ possui Ciclo Hamiltoniano}
\iff
G' \text{ possui rota do PCV com custo } \leq n.
$$

## Complexidade da transformação

O grafo completo $G'$ possui $O(n^2)$ arestas. A atribuição dos custos 1 e 2
pode ser realizada em $O(n^2)$, portanto a transformação é polinomial.
Depois dela, basta uma chamada ao software que resolve o PCV e uma comparação
do custo retornado com $n$.

Assim, o software existente para o problema B pode ser usado para resolver o
problema A por meio de um adaptador polinomial.

## Ponto extra: P = NP?

Não é possível apresentar atualmente uma prova aceita de que $P=NP$, pois
essa continua sendo uma questão em aberto da Ciência da Computação.

Entretanto, podemos fazer a seguinte afirmação condicional: a versão de decisão
do PCV é NP-completa. Se o software da empresa resolvesse todas as suas
instâncias em tempo polinomial, então o PCV estaria em $P$. Como todo problema
de $NP$ pode ser reduzido em tempo polinomial a um problema NP-completo, isso
implicaria $P=NP$.

O fato de o software resolver o PCV perfeitamente não basta, por si só, para
provar $P=NP$: ele pode produzir a resposta exata utilizando tempo
exponencial.

## Referências

- Material da aula: *NP-Completo & NP-Difícil*, especialmente a definição de
  redução polinomial apresentada nos slides 37 a 39.
- Clay Mathematics Institute. [P vs NP](https://www.claymath.org/millennium/p-vs-np/).
