"""
Jogo da Velha (Tic Tac Toe) - Motor de IA
Este módulo implementa a lógica do Jogo da Velha e uma IA usando o algoritmo Minimax com poda alfa-beta.

"""

import math
from functools import lru_cache
from typing import Optional, Tuple, Set

# Constantes
X = "X"
O = "O"
EMPTY = None

# Tipo do tabuleiro imutável
Board = Tuple[
    Tuple[Optional[str], ...],
    Tuple[Optional[str], ...],
    Tuple[Optional[str], ...]
]


class TicTacToeEngine:
    """
    Motor principal da IA do Jogo da Velha.
    """

    @staticmethod
    def initial_state() -> Board:
        """
        Retorna o tabuleiro inicial vazio.
        """
        return (
            (EMPTY, EMPTY, EMPTY),
            (EMPTY, EMPTY, EMPTY),
            (EMPTY, EMPTY, EMPTY)
        )

    @staticmethod
    def player(board: Board) -> str:
        """
        Determina quem joga no próximo turno.
        """
        contagem_vazios = sum(
            linha.count(EMPTY)
            for linha in board
        )

        return X if contagem_vazios % 2 != 0 else O

    @staticmethod
    def actions(board: Board) -> Set[Tuple[int, int]]:
        """
        Retorna todas as jogadas possíveis.
        """
        return {
            (i, j)
            for i in range(3)
            for j in range(3)
            if board[i][j] == EMPTY
        }

    @staticmethod
    def result(
        board: Board,
        action: Tuple[int, int]
    ) -> Board:
        """
        Retorna um novo tabuleiro após aplicar uma ação.
        """
        if action not in TicTacToeEngine.actions(board):
            raise ValueError("Ação inválida.")

        jogador = TicTacToeEngine.player(board)

        novo_tabuleiro = [
            list(linha)
            for linha in board
        ]

        i, j = action
        novo_tabuleiro[i][j] = jogador

        return tuple(
            tuple(linha)
            for linha in novo_tabuleiro
        )

    @staticmethod
    def winner(board: Board) -> Optional[str]:
        """
        Verifica se existe um vencedor.
        """

        # Linhas
        for i in range(3):
            if (
                board[i][0] == board[i][1] ==
                board[i][2] != EMPTY
            ):
                return board[i][0]

        # Colunas
        for i in range(3):
            if (
                board[0][i] == board[1][i] ==
                board[2][i] != EMPTY
            ):
                return board[0][i]

        # Diagonal principal
        if (
            board[0][0] == board[1][1] ==
            board[2][2] != EMPTY
        ):
            return board[0][0]

        # Diagonal secundária
        if (
            board[0][2] == board[1][1] ==
            board[2][0] != EMPTY
        ):
            return board[0][2]

        return None

    @staticmethod
    def terminal(board: Board) -> bool:
        """
        Verifica se o jogo terminou.
        """
        return (
            TicTacToeEngine.winner(board) is not None
            or not any(
                EMPTY in linha
                for linha in board
            )
        )

    @staticmethod
    def utility(board: Board) -> int:
        """
        Retorna a utilidade final do estado.
        """
        vencedor = TicTacToeEngine.winner(board)

        if vencedor == X:
            return 1

        if vencedor == O:
            return -1

        return 0

    @staticmethod
    def minimax(
        board: Board
    ) -> Optional[Tuple[int, int]]:
        """
        Calcula a melhor jogada possível.
        """
        if TicTacToeEngine.terminal(board):
            return None

        jogador = TicTacToeEngine.player(board)

        melhor_acao = None

        if jogador == X:

            melhor_valor = -math.inf

            for acao in TicTacToeEngine.actions(board):

                valor = TicTacToeEngine.valor_minimo(
                    TicTacToeEngine.result(board, acao),
                    -math.inf,
                    math.inf
                )

                if valor > melhor_valor:
                    melhor_valor = valor
                    melhor_acao = acao

        else:

            melhor_valor = math.inf

            for acao in TicTacToeEngine.actions(board):

                valor = TicTacToeEngine.valor_maximo(
                    TicTacToeEngine.result(board, acao),
                    -math.inf,
                    math.inf
                )

                if valor < melhor_valor:
                    melhor_valor = valor
                    melhor_acao = acao

        return melhor_acao

    @staticmethod
    @lru_cache(maxsize=None)
    def valor_maximo(
        board: Board,
        alfa: float,
        beta: float
    ) -> float:
        """
        Calcula o valor máximo para X.
        """

        if TicTacToeEngine.terminal(board):
            return TicTacToeEngine.utility(board)

        valor = -math.inf

        for acao in TicTacToeEngine.actions(board):

            valor = max(
                valor,
                TicTacToeEngine.valor_minimo(
                    TicTacToeEngine.result(board, acao),
                    alfa,
                    beta
                )
            )

            alfa = max(alfa, valor)

            if beta <= alfa:
                break

        return valor

    @staticmethod
    @lru_cache(maxsize=None)
    def valor_minimo(
        board: Board,
        alfa: float,
        beta: float
    ) -> float:
        """
        Calcula o valor mínimo para O.
        """

        if TicTacToeEngine.terminal(board):
            return TicTacToeEngine.utility(board)

        valor = math.inf

        for acao in TicTacToeEngine.actions(board):

            valor = min(
                valor,
                TicTacToeEngine.valor_maximo(
                    TicTacToeEngine.result(board, acao),
                    alfa,
                    beta
                )
            )

            beta = min(beta, valor)

            if beta <= alfa:
                break

        return valor


# Exemplo de uso
if __name__ == "__main__":

    engine = TicTacToeEngine()

    tabuleiro = engine.initial_state()

    melhor_jogada = engine.minimax(tabuleiro)

    print("Melhor jogada:", melhor_jogada)