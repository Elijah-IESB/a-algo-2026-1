"""
Motor de IA para Jogo da Velha - Versão Ultra Otimizada.
Implementa Minimax, Poda Alpha-Beta e Memoização (Cache).
"""

import math
import copy
from typing import List, Tuple, Set, Optional, Dict

# Definições de constantes
X = "X"
O = "O"
EMPTY = None

# Memória global para evitar reprocessamento de estados já vistos
cache_de_estados: Dict[Tuple[Tuple[Optional[str], ...], ...], float] = {}

def initial_state() -> List[List[Optional[str]]]:
    """Retorna o tabuleiro 3x3 inicial vazio."""
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board: List[List[Optional[str]]]) -> str:
    """Determina de quem é o próximo turno."""
    contagem_vazios = sum(linha.count(EMPTY) for linha in board)
    return X if contagem_vazios % 2 != 0 else O

def actions(board: List[List[Optional[str]]]) -> Set[Tuple[int, int]]:
    """Retorna todas as coordenadas (i, j) disponíveis."""
    return {(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY}

def result(board: List[List[Optional[str]]], action: Tuple[int, int]) -> List[List[Optional[str]]]:
    """Simula o resultado de uma jogada num tabuleiro novo."""
    if action not in actions(board):
        raise Exception("Ação Inválida.")
    
    novo_tabuleiro = copy.deepcopy(board)
    novo_tabuleiro[action[0]][action[1]] = player(board)
    return novo_tabuleiro

def winner(board: List[List[Optional[str]]]) -> Optional[str]:
    """Verifica se existe um vencedor no tabuleiro atual."""
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY: return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != EMPTY: return board[0][i]
            
    if board[0][0] == board[1][1] == board[2][2] != EMPTY: return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY: return board[0][2]
    return None

def terminal(board: List[List[Optional[str]]]) -> bool:
    """Verifica se o jogo terminou."""
    return winner(board) is not None or not any(EMPTY in linha for linha in board)

def utility(board: List[List[Optional[str]]]) -> int:
    """Retorna a pontuação final do jogo."""
    vencedor = winner(board)
    if vencedor == X: return 1
    if vencedor == O: return -1
    return 0

def minimax(board: List[List[Optional[str]]]) -> Optional[Tuple[int, int]]:
    """Calcula a jogada ótima usando Minimax, Alpha-Beta e Cache."""
    if terminal(board):
        return None

    jogador_atual = player(board)
    alfa, beta = -math.inf, math.inf
    melhor_movimento = None

    if jogador_atual == X:
        melhor_valor = -math.inf
        for acao in actions(board):
            valor = valor_minimo(result(board, acao), alfa, beta)
            if valor > melhor_valor:
                melhor_valor, melhor_movimento = valor, acao
            alfa = max(alfa, melhor_valor)
    else:
        melhor_valor = math.inf
        for acao in actions(board):
            valor = valor_maximo(result(board, acao), alfa, beta)
            if valor < melhor_valor:
                melhor_valor, melhor_movimento = valor, acao
            beta = min(beta, melhor_valor)
            
    return melhor_movimento

def valor_maximo(tabuleiro: List[List[Optional[str]]], alfa: float, beta: float) -> float:
    """Calcula o valor máximo (X) com suporte a Cache."""
    id_estado = tuple(tuple(linha) for linha in tabuleiro)
    if id_estado in cache_de_estados:
        return cache_de_estados[id_estado]

    if terminal(tabuleiro):
        return utility(tabuleiro)

    v = -math.inf
    for acao in actions(tabuleiro):
        v = max(v, valor_minimo(result(tabuleiro, acao), alfa, beta))
        alfa = max(alfa, v)
        if beta <= alfa: break
    
    cache_de_estados[id_estado] = v
    return v

def valor_minimo(tabuleiro: List[List[Optional[str]]], alfa: float, beta: float) -> float:
    """Calcula o valor mínimo (O) com suporte a Cache."""
    id_estado = tuple(tuple(linha) for linha in tabuleiro)
    if id_estado in cache_de_estados:
        return cache_de_estados[id_estado]

    if terminal(tabuleiro):
        return utility(tabuleiro)

    v = math.inf
    for acao in actions(tabuleiro):
        v = min(v, valor_maximo(result(tabuleiro, acao), alfa, beta))
        beta = min(beta, v)
        if beta <= alfa: break
        
    cache_de_estados[id_estado] = v
    return v