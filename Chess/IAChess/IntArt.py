import random

pieceScore = {"K": 0, "Q": 10, "R": 5, "B": 3, "N": 3, "P": 1}
checkmate = 10000
stalemate = 500
DEPTH = 5

"""
Realiza un movimiento aleatorio.
"""
def findRandomMove(validMoves):
    return validMoves[random.randint(0, len(validMoves) - 1)]

"""
Busca el mejor movimiento posible.
"""
def findBestMove(gs, validMoves):
    turnMultiplier = 1 if gs.whiteToMove else -1
    oppMinMaxScore = checkmate
    bestPlayerMove = None
    random.shuffle(validMoves)

    for playerMove in validMoves:
        gs.makeMove(playerMove)
        oppMoves = gs.getValidMoves()

        if gs.staleMate:
            oppMaxScore = stalemate
        elif gs.checkMate:
            oppMaxScore = -checkmate
        else:
            oppMaxScore = -checkmate
            for oppMove in oppMoves:
                gs.makeMove(oppMove)
                gs.getValidMoves()
                if gs.checkMate:
                    score = checkmate
                elif gs.staleMate:
                    score = stalemate
                else:
                    score = -turnMultiplier * scoreMaterial(gs.board)
                if score > oppMaxScore:
                    oppMaxScore = score
                gs.undoMove()

        if oppMaxScore < oppMinMaxScore:
            oppMinMaxScore = oppMaxScore
            bestPlayerMove = playerMove

        gs.undoMove()

    return bestPlayerMove

def findBestMoveAlphaBeta(gs, validMoves):
    global nextMove
    nextMove = None
    alpha = -checkmate
    beta = checkmate
    findMoveAlphaBeta(gs, validMoves, DEPTH, gs.whiteToMove, alpha, beta)
    return nextMove

"""
Busca el mejor movimiento utilizando el algoritmo minimax con poda alfa-beta.
"""
def findMoveAlphaBeta(gs, validMoves, depth, whiteToMove, alpha, beta):
    global nextMove

    if depth == 0:
        return scoreMaterial(gs.board)

    if whiteToMove:
        maxScore = -checkmate
        for move in validMoves:
            gs.makeMove(move)
            nextMoves = gs.getValidMoves()
            score = findMoveAlphaBeta(gs, nextMoves, depth - 1, False, alpha, beta)
            if score > maxScore:
                maxScore = score
                if depth == DEPTH:
                    nextMove = move
            gs.undoMove()

            alpha = max(alpha, maxScore)
            if alpha >= beta:
                break

        return maxScore

    else:
        minScore = checkmate
        for move in validMoves:
            gs.makeMove(move)
            nextMoves = gs.getValidMoves()
            score = findMoveAlphaBeta(gs, nextMoves, depth - 1, True, alpha, beta)
            if score < minScore:
                minScore = score
                if depth == DEPTH:
                    nextMove = move
            gs.undoMove()

            beta = min(beta, minScore)
            if alpha >= beta:
                break

        return minScore

"""
Un puntaje positivo si es bueno para el blanco, negativo si es bueno para el negro.
"""
def scoreBoard(gs):
    if gs.checkMate:
        if gs.whiteToMove:
            return -checkmate
        else:
            return checkmate
    elif gs.staleMate:
        return stalemate

    score = 0
    for row in gs.board:
        for square in row:
            if square[0] == 'w':
                score += pieceScore[square[1]]
            elif square[0] == 'b':
                score -= pieceScore[square[1]]
    return score

"""
Valor del tablero en base al material disponible.
"""
def scoreMaterial(board):
    score = 0
    for row in board:
        for square in row:
            if square[0] == 'w':
                score += pieceScore[square[1]]
            elif square[0] == 'b':
                score -= pieceScore[square[1]]
    return score
