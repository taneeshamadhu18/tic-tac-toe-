import pygame
import sys
pygame.init()
WIDTH, HEIGHT = 600, 600
window=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LINE_COLOR = (50, 50, 50)
board = [["" for _ in range(3)] for _ in range(3)]
current_player="X"
game_over=False
CELL_SIZE = WIDTH // 3
font = pygame.font.Font(None, 100)
small_font = pygame.font.Font(None, 50)
def draw_board():
    # Draw the grid
    window.fill(WHITE)
    for row in range(1, 3):
        pygame.draw.line(window, LINE_COLOR, (0, CELL_SIZE * row), (WIDTH, CELL_SIZE * row), 5)
        pygame.draw.line(window, LINE_COLOR, (CELL_SIZE * row, 0), (CELL_SIZE * row, HEIGHT), 5)
    for row in range(3):
        for col in range(3):
            if board[row][col] != "":
                text = font.render(board[row][col], True, BLACK)
                window.blit(text, (col * CELL_SIZE + CELL_SIZE // 3, row * CELL_SIZE + CELL_SIZE // 5))
def check_winner():
    global game_over
    for row in range(3):
        if board[row][0]==board[row][1]==board[row][2] != "":
            game_over=True
            return board[row][0]
    for col in range(3):
        if board[0][col]==board[1][col]==board[2][col] != "":
            game_over=True
            return board[0][col]
    if board[0][0]==board[1][1]==board[2][2]!= "":
        game_over=True
        return board[0][0]
    if board[0][2]==board[1][1]==board[2][0]!="":
        game_over=True
        return board[0][2]
    if all(board[row][col]!="" for row in range(3) for col in range(3)):
        game_over=True
        return "Tie"
    return None
def reset_game():
    global board, current_player, game_over
    board = [["" for _ in range(3)] for _ in range(3)]
    current_player = "X"
    game_over = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            row = mouse_y // CELL_SIZE
            col = mouse_x // CELL_SIZE
            if board[row][col] == "":
                board[row][col] = current_player
                winner = check_winner()
                if winner:
                    print(f"{winner} wins!" if winner != "Tie" else "It's a tie!")
                current_player = "O" if current_player == "X" else "X"
        if game_over and event.type==pygame.KEYDOWN:
            if event.key==pygame.K_r:
                reset_game()
    draw_board()
    if game_over:
          result_text = f"{winner} wins! Press 'R' to reset." if winner != "Tie" else "It's a tie! Press 'R' to reset."
          result_surface = small_font.render(result_text, True, BLACK)
    window.blit(result_surface, (WIDTH // 6, HEIGHT - 50))
    pygame.display.update()
