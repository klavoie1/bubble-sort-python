import pygame

pygame.init()

# Window Size
window = pygame.display.set_mode((1000, 700))

# Current Working title for Window
pygame.display.set_caption("Bubble Sort Visualizer")

# Width of Individual bar
WIDTH = 20

# Height of Individual Bar (Data that is actually sorted through)
height = [150, 70, 80, 51, 320, 46, 20, 120, 160, 154,
          255, 142, 302, 34, 67, 105, 75, 123]

clock = pygame.time.Clock()

# Initial Position
x = 30
y = 30

running = True

def show(height):
    for i in range(len(height)):
        pygame.draw.rect(window, (255, 255, 0), (x + 35 * i, y, WIDTH, height[i]))

while running:
    run = False

    key = pygame.key.get_pressed()
    pygame.key.get_focused()

    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if key[pygame.K_SPACE]:
        run = True

    if key[pygame.K_q]:
        pygame.quit()

    if run == False:
        window.fill((0, 0, 0))
        show(height)
        pygame.display.update()

    else:
        for i in range(len(height) - 1):
            for j in range(len(height) - i -1):
                if height[j] > height[j + 1]:
                    b = height[j]
                    height[j] = height[j + 1]
                    height[j + 1] = b
                
                window.fill((0, 0, 0))

                show(height)

                pygame.time.delay(30)

                pygame.display.update()

pygame.quit()