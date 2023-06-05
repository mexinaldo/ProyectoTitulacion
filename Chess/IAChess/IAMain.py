import pygame as pygame
import time
from Chess.IAChess import IntArt
from Chess.IAChess import IAEngine
from pygame import mixer

Board_width = Board_height = 710
MoveLogPanelWidth = 350
MoveLogPanelHeight = Board_height
keyboardactionsWitdth = 710
keyboardactionHeight = 100
dimension = 8
sq_Size = 710 // dimension
max_fps = 60
images = {}


"""
Para inicializar las imagenes de las piezas.
"""
def loadImage():
    pieces = ['bP', 'bR', 'bN', 'bB', 'bQ', 'bK', 'wP', 'wR', 'wN', 'wB', 'wQ', 'wK']
    for piece in pieces:
        images[piece] = pygame.transform.scale(pygame.image.load("C:/proyectoChess/Chess/images/" + piece + ".png"),
                                               (sq_Size, sq_Size))

def main():
    pygame.init()
    pygame.mixer.init()
    fullscreen = False
    if fullscreen:
        screen = pygame.display.set_mode((Board_width + MoveLogPanelWidth, Board_height + keyboardactionHeight),
                                         pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode((Board_width + MoveLogPanelWidth, Board_height + keyboardactionHeight))
    clock = pygame.time.Clock()
    screen.fill(pygame.Color("white"))
    moveLogFont = pygame.font.SysFont("Helvetica", 15, False, False)
    gs = IAEngine.GameState()
    validMoves = gs.getValidMoves()
    moveMade = False
    animate = False
    loadImage()
    run = True
    sqSelect = ()
    playerClick = []  # Conteo de los clicks por parejas.
    gameOver = False
    playerOne = True  # Si el jugador juega blancas, será True, si no, no.
    playerTwo = False  # Igual que con playerOne, pero orientado a las negras.
    victory_sound_played = False
    while run:  # Para correr el juego.
        humanTurn = (gs.whiteToMove and playerOne) or (not gs.whiteToMove and playerTwo)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                run = False
            elif e.type == pygame.MOUSEBUTTONDOWN:
                if not gameOver and humanTurn:
                    location = pygame.mouse.get_pos()  # La posición del mouse en el eje X e Y.
                    col = location[0] // sq_Size
                    row = location[1] // sq_Size
                    if sqSelect == (row, col):  # El usurio hace click dos veces en el mismo sitio y se limpian.
                        sqSelect = ()
                        playerClick = []
                    else:
                        sqSelect = (row, col)
                        playerClick.append(sqSelect)
                    if len(playerClick) == 2:  # Después de 2 clicks.
                        move = IAEngine.Move(playerClick[0], playerClick[1], gs.board)


                        for i in range(len(validMoves)):
                            if move == validMoves[i]:  # Para verificar la validez de un movimiento.
                                gs.makeMove(validMoves[i])
                                moveMade = True
                                animate = True
                                sqSelect = ()
                                playerClick = []
                        if not moveMade:
                            playerClick = [sqSelect]
            elif e.type == pygame.KEYDOWN:  # Se deshace el movimiento hecho de pulsarse z.
                if e.key == pygame.K_z:
                    gs.undoMove()
                    moveMade = True
                    animate = False
                    gameOver = False
                if e.key == pygame.K_r:  # Se reinicia el tablero.
                    gs = IAEngine.GameState()
                    validMoves = gs.getValidMoves()
                    sqSelect = ()
                    playerClick = []
                    moveMade = True
                    animate = False
                    gameOver = False

                if e.key == pygame.K_e:
                    print("salir")
                    pygame.display.quit()
                    pygame.quit()
                    from Chess.util.ChessToMenu import ChessToMenu
                    ChessToMenu()

                if e.key == pygame.K_F11:
                    fullscreen = not fullscreen
                    if fullscreen:
                        screen = pygame.display.set_mode((Board_width + MoveLogPanelWidth,
                                                          Board_height + keyboardactionHeight),
                                                         pygame.FULLSCREEN)
                        moveLogFont = pygame.font.SysFont("Helvetica", 20, False, False)
                    else:
                        screen = pygame.display.set_mode((Board_width + MoveLogPanelWidth,
                                                          Board_height + keyboardactionHeight))
                        moveLogFont = pygame.font.SysFont("Helvetica", 15, False, False)

        # Movimientos de la I.A.
        if not gameOver and not humanTurn:
            time.sleep(2)
            AIMove = IntArt.findBestMove(gs, validMoves)
            if AIMove is None:
                AIMove = IntArt.findRandomMove(validMoves)
            gs.makeMove(AIMove)
            moveMade = True
            animate = True

        if moveMade:
            validMoves = gs.getValidMoves()
            mixer.music.load("C:\\proyectoChess\\Chess\\aprender\\sounds\\movimiento.wav")
            mixer.music.play()
            moveMade = False
            animate = False
            if animate:
                animateMove(gs.moveLog[1], screen, gs.board, clock)
        drawGameStage(screen, gs, validMoves, sqSelect, moveLogFont)

        # Cuando termine la partida en empate con un jaque mate.
        if gs.checkMate:
            gameOver = True
            if gs.whiteToMove:
                drawText(screen, 'Victoria de las negras por jaque mate.')

            else:
                drawText(screen, 'Victoria de las Blancas por jaque mate.')
            if not victory_sound_played and gs.checkMate:
                mixer.music.load("C:/proyectoChess/Chess/aprender/sounds/win.mp3")
                mixer.music.play()
                victory_sound_played = True
        elif gs.staleMate:
            drawText(screen, 'Jaque.')

        clock.tick(max_fps)
        pygame.display.flip()


"""
Resalte de las casillas disponibles conforme al moviento de las piezas.
"""


def highlightSquares(screen, gs, validMoves, sqSelected):
    if sqSelected != ():
        r, c = sqSelected
        if gs.board[r][c][0] == ('w' if gs.whiteToMove else 'b'):  # Pieza seleccionada.
            # Resalte de las casillas elegidas.
            s = pygame.Surface((sq_Size, sq_Size))
            s.set_alpha(200)
            s.fill(pygame.Color('darkgoldenrod1'))
            screen.blit(s, (c * sq_Size, r * sq_Size))
            # Resalte de los movientos desde aquella casilla.
            s.fill(pygame.Color('yellow1'))
            for move in validMoves:
                if move.startRow == r and move.startCol == c:
                    screen.blit(s, (sq_Size * move.endCol, sq_Size * move.endRow))


"""
Esto dibuja todos los elementos del juego, el tablero entero con piezas, el tablero y las piezas, respectivamente. El último ejecuta el programa.
"""


def drawGameStage(screen, gs, validMoves, sqSelected, moveLogFont):
    drawBoard(screen)
    highlightSquares(screen, gs, validMoves, sqSelected)
    drawPieces(screen, gs.board)
    drawMoveLog(screen, gs, moveLogFont)
    drawkeyboardactions(screen, gs, moveLogFont)


def drawBoard(screen):
    global colors
    colors = [pygame.Color("white"), pygame.Color("seagreen")]
    for r in range(dimension):  # Para las filas.
        for c in range(dimension):  # Para las columnas.
            color = colors[((r + c) % 2)]
            pygame.draw.rect(screen, color, pygame.Rect(c * sq_Size, r * sq_Size, sq_Size, sq_Size))


def drawPieces(screen, board):
    for r in range(dimension):  # Para las filas.
        for c in range(dimension):  # Para las columnas.
            piece = board[r][c]
            if piece != "--":  # Para cuando la casilla no está vacía.
                screen.blit(images[piece], pygame.Rect(c * sq_Size, r * sq_Size, sq_Size, sq_Size))


def drawkeyboardactions(screen, gs, font):
    keyboardRect = pygame.Rect(0, 710, keyboardactionsWitdth, keyboardactionHeight)
    pygame.draw.rect(screen, pygame.Color("black"), keyboardRect)
    mensaje1 = 'Retroceder un movimiento: Tecla "Z"'
    mensaje2 = 'Reiniciar juego: Tecla "R"'
    mensaje3 = 'Salir del juego: Tecla "E"'

    textObject1 = font.render(mensaje1, True, pygame.Color('white'))
    textObject2 = font.render(mensaje2, True, pygame.Color('white'))
    textObject3 = font.render(mensaje3, True, pygame.Color('white'))

    padding = 10
    movesPerRow = 3
    textY = padding
    lineSpacing = 10

    screen.blit(textObject1, keyboardRect.move(padding, textY))
    textY += textObject1.get_height() + lineSpacing
    screen.blit(textObject2, keyboardRect.move(padding, textY))
    textY += textObject2.get_height() + lineSpacing
    screen.blit(textObject3, keyboardRect.move(padding, textY))
    textY += textObject3.get_height() + lineSpacing


def drawMoveLog(screen, gs, font):
    moveLogRect = pygame.Rect(Board_width, 0, MoveLogPanelWidth, MoveLogPanelHeight + keyboardactionHeight)
    pygame.draw.rect(screen, pygame.Color("black"), moveLogRect)
    moveLog = gs.moveLog
    moveTexts = []

    mensaje1 = "¡Bienvenido al registro de movimientos!"
    mensaje2 = "Aquí se mostrarán los movimientos realizados."
    mensaje3 = "Haz un movimiento válido para registrar tu jugada."

    textObject1 = font.render(mensaje1, True, pygame.Color('white'))
    textObject2 = font.render(mensaje2, True, pygame.Color('white'))
    textObject3 = font.render(mensaje3, True, pygame.Color('white'))

    padding = 10
    movesPerRow = 3
    textY = padding
    lineSpacing = 10

    screen.blit(textObject1, moveLogRect.move(padding, textY))
    textY += textObject1.get_height() + lineSpacing
    screen.blit(textObject2, moveLogRect.move(padding, textY))
    textY += textObject2.get_height() + lineSpacing
    screen.blit(textObject3, moveLogRect.move(padding, textY))
    textY += textObject3.get_height() + lineSpacing

    for i in range(0, len(moveLog), 2):
        moveString = str(i // 2 + 1) + ".- " + str(moveLog[i]) + "  "
        if i + 1 < len(moveLog):
            moveString += str(moveLog[i + 1]) + "  "
        moveTexts.append(moveString)

    for i in range(0, len(moveTexts), movesPerRow):
        text = ""
        for j in range(movesPerRow):
            if i + j < len(moveTexts):
                text += moveTexts[i + j]
        textObject = font.render(text, True, pygame.Color('white'))
        textLocation = moveLogRect.move(padding, textY)
        screen.blit(textObject, textLocation)
        textY += textObject.get_height() + lineSpacing


def animateMove(move, screen, board, clock):
    global colors
    dR = move.endRow - move.startRow
    dC = move.endCol - move.startCol
    framesPerSquare = 30
    frameCount = (abs(dR) + abs(dC)) * framesPerSquare
    for frame in range(frameCount + 1):
        r, c = (move.startRow + dR * frame / frameCount, move.startCol + dC * frame / frameCount)
        drawBoard(screen)
        drawPieces(screen, board)
        color = colors[(move.endRow + move.endCol) % 2]
        endSquare = pygame.Rect(move.endCol * sq_Size, move.endRow * sq_Size, sq_Size, sq_Size)
        pygame.draw.rect(screen, color, endSquare)
        if move.pieceCaptured != '--' and move.pieceCaptured in images:
            screen.blit(images[move.pieceCaptured], endSquare)

        screen.blit(images[move.pieceMoved], pygame.Rect(c * sq_Size, r * sq_Size, sq_Size, sq_Size))
        pygame.display.flip()
        clock.tick(60)


def drawText(screen, text):
    font = pygame.font.SysFont("Helvetica", 32, True, False)
    textObj = font.render(text, False, pygame.Color('Black'))
    textLocation = pygame.Rect(0, 0, Board_width,
                                Board_height).move(Board_width / 2 - textObj.get_width() / 2,
                                                   Board_height / 2 - textObj.get_height() / 2)
    screen.blit(textObj, textLocation)
    textObj = font.render(text, False, pygame.Color('Gray'))
    screen.blit(textObj, textLocation.move(2, 2))


class innit():
    def __init__(self):
        main()
