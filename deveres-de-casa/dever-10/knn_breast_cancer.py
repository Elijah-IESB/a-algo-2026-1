"""Aplicacao do algoritmo KNN no Breast Cancer Wisconsin."""

from sklearn.datasets import load_breast_cancer
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


def avaliar_knn(x_treino, x_teste, y_treino, y_teste):
    """Treina e avalia KNN com diferentes valores de K e metricas."""
    valores_k = [1, 3, 5]
    metricas = ["euclidean", "manhattan"]
    resultados = []

    for valor_k in valores_k:
        for metrica in metricas:
            modelo = Pipeline(
                [
                    ("normalizador", StandardScaler()),
                    (
                        "knn",
                        KNeighborsClassifier(
                            n_neighbors=valor_k,
                            metric=metrica,
                        ),
                    ),
                ]
            )

            modelo.fit(x_treino, y_treino)
            previsoes = modelo.predict(x_teste)
            acuracia = accuracy_score(y_teste, previsoes)

            resultados.append(
                {
                    "k": valor_k,
                    "metrica": metrica,
                    "acuracia": acuracia,
                    "relatorio": classification_report(
                        y_teste,
                        previsoes,
                        target_names=["maligno", "benigno"],
                    ),
                }
            )

    return resultados


def imprimir_resultados(resultados):
    """Imprime a comparacao de acuracia entre as combinacoes."""
    print("Resultados do KNN no Breast Cancer Wisconsin")
    print("=" * 60)

    for resultado in resultados:
        print(
            f"K = {resultado['k']} | "
            f"Metrica = {resultado['metrica']} | "
            f"Acuracia = {resultado['acuracia']:.4f}"
        )

    melhor_resultado = max(resultados, key=lambda item: item["acuracia"])

    print()
    print("Melhor combinacao:")
    print(
        f"K = {melhor_resultado['k']} | "
        f"Metrica = {melhor_resultado['metrica']} | "
        f"Acuracia = {melhor_resultado['acuracia']:.4f}"
    )
    print()
    print("Relatorio de classificacao da melhor combinacao:")
    print(melhor_resultado["relatorio"])


def main():
    """Executa a atividade de classificacao com KNN."""
    dados = load_breast_cancer()
    x_treino, x_teste, y_treino, y_teste = train_test_split(
        dados.data,
        dados.target,
        test_size=0.2,
        random_state=42,
        stratify=dados.target,
    )

    resultados = avaliar_knn(x_treino, x_teste, y_treino, y_teste)
    imprimir_resultados(resultados)


if __name__ == "__main__":
    main()
