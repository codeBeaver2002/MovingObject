import pygame

pygame.init()


win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Moving rectangle")


x = 200
y = 200


width = 20
height = 20


vel = 10


run = True

clock = pygame.time.Clock()
while run:
    clock.tick(60)
    pygame.time.delay(10)

    # iterate over the list of Event objects
    # that was returned by pygame.event.get() method.
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False
    # stores keys pressed
    keys = pygame.key.get_pressed()

    # if left arrow key is pressed
    if keys[pygame.K_LEFT] and x > 0:
        # decrement in x co-ordinate
        x -= vel

    # if left arrow key is pressed
    if keys[pygame.K_RIGHT] and x < 500 - width:
        # increment in x co-ordinate
        x += vel

    # if left arrow key is pressed
    if keys[pygame.K_UP] and y > 0:
        # decrement in y co-ordinate
        y -= vel

    # if left arrow key is pressed
    if keys[pygame.K_DOWN] and y < 500 - height:
        # increment in y co-ordinate
        y += vel

    # completely fill the surface object
    # with black colour
    win.fill((0, 0, 0))

    # drawing object on screen which is rectangle here
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))

    # it refreshes the window
    pygame.display.update()

pygame.quit()