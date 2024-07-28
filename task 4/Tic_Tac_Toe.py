print("<<<<<<<<<<<--Welcome To Simple To Tic Tac Toe-->>>>>>>>>>>")
import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_SIZE = 300
GRID_SIZE = SCREEN_SIZE // 3
LINE_WIDTH = 15
CIRCLE_RADIUS = GRID_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = GRID_SIZE // 4

# Colors
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (84, 84, 84)

# Screen setup
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption('Tic Tac Toe')
screen.fill(BG_COLOR)

# Game board
board = [[None] * 3 for _ in range(3)]

# Player
player = 'X'

def draw_lines():
    # Horizontal lines
    for i in range(1, 3):
        pygame.draw.line(screen, LINE_COLOR, (0, GRID_SIZE * i), (SCREEN_SIZE, GRID_SIZE * i), LINE_WIDTH)
    
    # Vertical lines
    for i in range(1, 3):
        pygame.draw.line(screen, LINE_COLOR, (GRID_SIZE * i, 0), (GRID_SIZE * i, SCREEN_SIZE), LINE_WIDTH)

def draw_figures():
    for row in range(3):
        for col in range(3):
            if board[row][col] == 'O':
                pygame.draw.circle(screen, CIRCLE_COLOR, (int(col * GRID_SIZE + GRID_SIZE // 2), int(row * GRID_SIZE + GRID_SIZE // 2)), CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 'X':
                pygame.draw.line(screen, CROSS_COLOR, (col * GRID_SIZE + SPACE, row * GRID_SIZE + GRID_SIZE - SPACE), (col * GRID_SIZE + GRID_SIZE - SPACE, row * GRID_SIZE + SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, (col * GRID_SIZE + SPACE, row * GRID_SIZE + SPACE), (col * GRID_SIZE + GRID_SIZE - SPACE, row * GRID_SIZE + GRID_SIZE - SPACE), CROSS_WIDTH)

def check_winner(player):
    # Check rows
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] == player:
            return True

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

def restart():
    global board, player
    board = [[None] * 3 for _ in range(3)]
    player = 'X'
    screen.fill(BG_COLOR)
    draw_lines()

# Main loop
draw_lines()
game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0] // GRID_SIZE
            mouseY = event.pos[1] // GRID_SIZE

            if board[mouseY][mouseX] is None:
                board[mouseY][mouseX] = player
                draw_figures()
                if check_winner(player):
                    game_over = True
                player = 'O' if player == 'X' else 'X'

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                game_over = False

    pygame.display.update()
