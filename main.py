from PIL import Image
import pygame
import time

WIDTH = 1200
HEIGHT = 1000


def pygame_init():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
    game_screen = pygame.Surface(screen.get_size())
    game_screen.convert()

    return screen


def display_text(screen, text ,x ,y):
    font = pygame.font.SysFont('arial', 3)
    words = str(text)
    text = font.render(words, True, (255,255,255))
    textRect = text.get_rect()
    textRect.topleft = (x, y)
    screen.blit(text, textRect)


def get_average(pixs, width, height, block_size):
    avg_arr = []
    for i in range(0, width, block_size):
        avg_arr.append([])
        for j in range(0, height, block_size):
            sum1 = 0
            for k in range(block_size):
                for l in range(block_size):
                    sum1 += pixs[i + k][j + l]

            avg_arr[-1].append(int(sum1 / (block_size*block_size)))
    return avg_arr


def image_to_text(src, block_size, multiplier, color):
    im = Image.open(src, "r")
    width, height = im.size
    pixls = list(im.getdata())

    width = width - width % block_size
    height = height - height % block_size
    print(width, height)

    pixs = []
    for i in range(width):
        pixs.append([])
        for j in range(height):
            pixs[-1].append(pixls[j * width + i])

    for i in range(width):
        for j in range(height):
            pixs[i][j] = round((pixs[i][j][0] + pixs[i][j][1] + pixs[i][j][2]) / 3)

    if color == "b":
        chars = "N@#8653?!ac:+-. "
    elif color == "w":
        chars = " .-+:ca!?3568#@N"
    avg_arr = get_average(pixs, width, height, block_size)


    lines = []

    for i in range(round(height / block_size)):
        line = ""
        for j in range(round(width / block_size)):
            line += chars[int(avg_arr[j][i] / 16)] * multiplier
        lines.append(line)

    return lines


text = image_to_text("waltuh.jpg", 5, 2, "b")

# for i in range(len(text)):
#    for j in range(len(text[0])):
#        print(text[i][j], end="")
#    print("")

with open(r'C:\Users\Paz Malul\Desktop\pazon.txt', 'w') as the_file:
   for i in range(len(text)):
       the_file.write(text[i]+'\n')
