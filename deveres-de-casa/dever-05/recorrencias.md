# Resolução de Recorrências

Este documento apresenta a resolução de recorrências utilizando o Teorema Mestre.

---

## 1) T(n) = 2T(n/4) + √n

Parâmetros:
- a = 2
- b = 4
- f(n) = n^(1/2)

Cálculo:
n^(log_b a) = n^(log₄2) = n^(1/2)

Comparação:
f(n) = Θ(n^(1/2)) = Θ(n^(log_b a))

Caso:
Caso 2 do Teorema Mestre

Resultado:
T(n) = Θ(√n log n)

---

## 2) T(n) = 2T(n/4) + n

Parâmetros:
- a = 2
- b = 4
- f(n) = n

Cálculo:
n^(log_b a) = n^(log₄2) = n^(1/2)

Comparação:
f(n) cresce mais rápido que n^(1/2)

Caso:
Caso 3 do Teorema Mestre

Resultado:
T(n) = Θ(n)

---

## 3) T(n) = 16T(n/4) + n²

Parâmetros:
- a = 16
- b = 4
- f(n) = n²

Cálculo:
n^(log_b a) = n^(log₄16) = n²

Comparação:
f(n) = Θ(n²) = Θ(n^(log_b a))

Caso:
Caso 2 do Teorema Mestre

Resultado:
T(n) = Θ(n² log n)