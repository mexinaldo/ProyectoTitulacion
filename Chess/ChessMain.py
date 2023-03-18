"""
this is our main driver file. it will be responsible  for handling user input and displaying the current GameState object
Este es nuestro archivo de controlador principal. Será responsable de manejar la entrada del usuario y mostrar el objeto GameState actual
"""

import pygame as pygame
from Chess import ChessEngine

Board_width = Board_height = 800
MoveLogPanelWidth = 250
MoveLogPanelHeight = Board_height
dimension = 8  # Dimensión del tablero.
sq_Size = 800// dimension  # Dimensiones de las casillas.
max_fps = 60  # Para las animaciones.
images = {}

"""
Initialize a global dictionary of images. This will be called exactly once in the main
"""


def loadImages():
    pieces = ['wP', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bP', 'bR', 'bN', 'bB', 'bK', 'bQ']
    for piece in pieces:
        images[piece] = pygame.transform.scale(pygame.image.load("C:/proyectoChess/Chess/images/" + piece + ".png"),
                                               (sq_Size, sq_Size))
        # NOTE: we access an image by saying  'IMAGES['wp']'


'''
the main driver for our code. this will handle  user input and updating the graphics
'''


def main():
    pygame.init()
    fullscreen = False
    if fullscreen:
        screen = pygame.display.set_mode((Board_width + MoveLogPanelWidth, Board_height), pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode((Board_width + MoveLogPanelWidth, Board_height))
    clock = pygame.time.Clock()
    screen.fill(pygame.Color("white"))
    moveLogFont = pygame.font.SysFont("Helvetica", 15, False, False)
    gs = ChessEngine.GameState()
    validMoves = gs.getValidMoves()
    moveMade = False  # flag variable for when a move is made
    animate = False
    loadImages()  # only do this once, before  the while loop
    running = True
    sqSelected = ()  # no square is selected, keep track of the last click of the user (tuple:(row, col))
    playerClicks = []  # keep track of player clicks (two tuples: [(6,6), (4,4)])
    gameOver = False
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
                # mouse handler
            elif e.type == pygame.MOUSEBUTTONDOWN:
                if not gameOver:
                    location = pygame.mouse.get_pos()  # this is for location of mouse (x, y)
                    col = location[0] // sq_Size
                    row = location[1] // sq_Size
                    if sqSelected == (
                            row,
                            col) or col >= 8:  # this is for verification if the user puts the same location or square
                        sqSelected = ()  # deselect
                        playerClicks = []  # clear the player click
                    else:
                        sqSelected = (row, col)
                        playerClicks.append(sqSelected)  # append for both 1st and  2nd clicks
                    if len(playerClicks) == 2:  # this is after 2nd click
                        move = ChessEngine.Move(playerClicks[0], playerClicks[1], gs.board)
                        print(move.getChessNotation())

                        for i in range(len(validMoves)):
                            if move == validMoves[i]:
                                gs.makeMove(validMoves[i])
                                moveMade = True
                                animate = True
                                sqSelected = ()  # reset user cliks
                                playerClicks = []
                        if not moveMade:
                            playerClicks = [sqSelected]

                # key handlers
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_z:  # undo when 'z' is pressed
                    gs.undoMove()
                    moveMade = True
                    animate = False
                    gameOver = False

                if e.key == pygame.K_r:
                    gs = ChessEngine.GameState()
                    validMoves = gs.getValidMoves()
                    sqSelected = ()
                    playerClicks = []
                    moveMade = False
                    animate = False
                    gameOver = False

                if e.key == pygame.K_e:
                    print("salir")
                    from Chess.Forms.form_login import FormLogin
                    pygame.display.quit()
                    FormLogin()

                if e.key == pygame.K_F11:
                    fullscreen = not fullscreen
                    if fullscreen:
                        screen = pygame.display.set_mode((Board_width + MoveLogPanelWidth, Board_height), pygame.FULLSCREEN)
                        moveLogFont = pygame.font.SysFont("Helvetica", 20, False, False)
                    else:
                        screen = pygame.display.set_mode((Board_width + MoveLogPanelWidth, Board_height))
                        moveLogFont = pygame.font.SysFont("Helvetica", 15, False, False)

        if moveMade:
            if animate:
                animateMove(gs.moveLog[-1], screen, gs.board, clock)
            validMoves = gs.getValidMoves()
            moveMade = False
            animate = False

        drawGameState(screen, gs, validMoves, sqSelected, moveLogFont)
        if gs.checkMate or gs.staleMate:

            if gs.staleMate:
                drawEndGameText(screen, "Jaque")
            else:
                if gs.whiteToMove:
                    drawEndGameText(screen, "negras ganan por jaque mate")
                else:
                    drawEndGameText(screen, "blancas ganan por jaque mate")
                gameOver = True

        clock.tick(max_fps)
        pygame.display.flip()


''''
this is responsible for  all the graphics within a current game state.
'''


def drawGameState(screen, gs, validMoves, sqSelected, moveLogFont):
    drawBoard(screen)
    highlightSquares(screen, gs, validMoves, sqSelected)
    drawPieces(screen, gs.board)
    drawMoveLog(screen, gs, moveLogFont)


'''
highlight square selected and moves for piece selected
'''


def highlightSquares(screen, gs, validMoves, sqSelected):
    if sqSelected != ():
        r, c = sqSelected
        if gs.board[r][c][0] == ('w' if gs.whiteToMove else 'b'):
            s = pygame.Surface((sq_Size, sq_Size))
            s.set_alpha(200)
            s.fill(pygame.Color('darkgoldenrod1'))
            screen.blit(s, (c * sq_Size, r * sq_Size))
            s.fill(pygame.Color('yellow1'))
            for move in validMoves:
                if move.startRow == r and move.startCol == c:
                    screen.blit(s, (move.endCol * sq_Size, move.endRow * sq_Size))


'''
Draw the squares on the board. the top square is always  light
'''

def drawBoard(screen):
    global colors
    colors = [pygame.Color("white"), pygame.Color("seagreen")]
    for r in range(dimension):
        for c in range(dimension):
            color = colors[((r + c) % 2)]
            pygame.draw.rect(screen, color, pygame.Rect(c * sq_Size, r * sq_Size, sq_Size, sq_Size))


'''
Draw the pieces on the board using  the current GameState.board
'''


def drawPieces(screen, board):
    for r in range(dimension):
        for c in range(dimension):
            piece = board[r][c]
            if piece != "--":  # not empty square
                screen.blit(images[piece], pygame.Rect(c * sq_Size, r * sq_Size, sq_Size, sq_Size))


'''
Draws the move log
'''


def drawMoveLog(screen, gs, font):
    moveLogRect = pygame.Rect(Board_width, 0, MoveLogPanelWidth, MoveLogPanelHeight)
    pygame.draw.rect(screen, pygame.Color("black"), moveLogRect)
    moveLog = gs.moveLog
    moveTexts = []

    for i in range(0, len(moveLog), 2):
        moveString = str(i // 2 + 1) + ".- " + str(moveLog[i]) + "  "
        if i + 1 < len(moveLog):
            moveString += str(moveLog[i + 1]) + "  "
        moveTexts.append(moveString)

    padding = 5
    movesPerRow = 2
    textY = padding
    lineSpacing = 2
    for i in range(0, len(moveTexts), movesPerRow):
        text = ""
        for j in range(movesPerRow):
            if i + j < len(moveTexts):
                text += moveTexts[i + j]
        textObject = font.render(text, True, pygame.Color('white'))
        textLocation = moveLogRect.move(padding, textY)
        screen.blit(textObject, textLocation)
        textY += textObject.get_height() + lineSpacing


'''
animating a move
'''


def animateMove(move, screen, board, clock):
    global colors
    dR = move.endRow - move.startRow
    dC = move.endCol - move.startCol
    framesPerSquare = 10
    frameCount = (abs(dR) + abs(dC)) * framesPerSquare
    for frame in range(frameCount + 1):
        r, c = (move.startRow + dR * frame / frameCount, move.startCol + dC * frame / frameCount)
        drawBoard(screen)
        drawPieces(screen, board)
        color = colors[(move.endRow + move.endCol) % 2]
        endSquare = pygame.Rect(move.endCol * sq_Size, move.endRow * sq_Size, sq_Size, sq_Size)
        pygame.draw.rect(screen, color, endSquare)
        if move.pieceCaptured != '--':
            screen.blit(images[move.pieceCaptured], endSquare)

        screen.blit(images[move.pieceMoved], pygame.Rect(c * sq_Size, r * sq_Size, sq_Size, sq_Size))
        pygame.display.flip()
        clock.tick(60)


def drawEndGameText(screen, text):
    font = pygame.font.SysFont("Helvetica", 32, True, False)
    textObject = font.render(text, False, pygame.Color('Black'))
    textLocation = pygame.Rect(0, 0, Board_width, Board_height).move(Board_width / 2 - textObject.get_width() / 2,
                                                                     Board_height / 2 - textObject.get_height() / 2)
    screen.blit(textObject, textLocation)
    textObject = font.render(text, False, pygame.Color('Gray'))
    screen.blit(textObject, textLocation.move(2, 2))


class innit():
    def __init__(self):
        main()
