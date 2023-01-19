import pygame

# Initialize Pygame
pygame.init()

# Set the window size and caption
size = (512, 512)
caption = "Chess Board"
screen = pygame.display.set_mode(size)
pygame.display.set_caption(caption)

# Create a 2D array to represent the chess board
board = [[0 for x in range(8)] for y in range(8)]

# Fill the array with the appropriate chess pieces
for i in range(8):
    board[i][1] = "p"
    board[i][6] = "P"

board[0][0] = "r"
board[1][0] = "n"
board[2][0] = "b"
board[3][0] = "q"
board[4][0] = "k"
board[5][0] = "b"
board[6][0] = "n"
board[7][0] = "r"

board[0][7] = "R"
board[1][7] = "N"
board[2][7] = "B"
board[3][7] = "Q"
board[4][7] = "K"
board[5][7] = "B"
board[6][7] = "N"
board[7][7] = "R"

# Create a loop to update the screen
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the chess board
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                color = (255, 255, 255)
            else:
                color = (100, 100, 100)
            pygame.draw.rect(screen, color, (i*64, j*64, 64, 64))

    # Draw the chess pieces on the board
    for i in range(8):
        for j in range(8):
            if board[i][j] != 0:
                # Load the appropriate image for the piece
                if board[i][j] == "p":
                    img = pygame.image.load("bpawn.png")
                elif board[i][j] == "r":
                    img = pygame.image.load("brook.png")
                elif board[i][j] == "n":
                    img = pygame.image.load("bknight.png")
                elif board[i][j] == "b":
                    img = pygame.image.load("bbishop.png")
                elif board[i][j] == "q":
                    img = pygame.image.load("bqueen.png")
                elif board[i][j] == "k":
                    img = pygame.image.load("bking.png")
                
                elif board[i][j] == "P":
                    img = pygame.image.load("PAWN.png")
                elif board[i][j] == "R":
                    img = pygame.image.load("ROOK.png")
                elif board[i][j] == "N":
                    img = pygame.image.load("KNIGHT.png")
                elif board[i][j] == "B":
                    img = pygame.image.load("BISHOP.png")
                elif board[i][j] == "Q":
                    img = pygame.image.load("QUEEN.png")
                elif board[i][j] == "K":
                    img = pygame.image.load("KING.png")

                # Add the rest of the chess pieces
                screen.blit(img, (i*64, j*64))

    # Update the screen
    pygame.display.flip()

# Quit Pygame
pygame.quit()
