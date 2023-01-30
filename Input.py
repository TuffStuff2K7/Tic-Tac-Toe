def passInput():

    # import modules

    import pygame
    import sys

    password = "harifullmarks"

    # initialize pygame

    pygame.init()

    clock = pygame.time.Clock()

    # to set width of the game window

    width = 400

    # to set height of the game window

    height = 100

    pygame.display.set_caption("Enter password to continue:")

    icon = pygame.image.load("./Assets/Icon.png")

    pygame.display.set_icon(icon)

    screen = pygame.display.set_mode((width, height + 100), 0, 32)

    # importing font from files
    font = pygame.font.Font("./Assets/RobotoMono-Regular.ttf", 30)

    user_text = ""

    # create rectangle for input
    input_rect = pygame.Rect(width/2 - 150, height/2, 300, 40)

    # storing colors for the input box
    color_active = pygame.Color('lightskyblue3')
    color_passive = pygame.Color(26, 18, 11)
    color = color_passive

    active = False

    while True:

        for event in pygame.event.get():

        # if user types QUIT then the screen will close

            if event.type == pygame.QUIT:

                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if input_rect.collidepoint(event.pos):

                    active = True

                else:

                    active = False

            if active:

                if event.type == pygame.KEYDOWN:

                    # check for backspace
                    if event.key == pygame.K_BACKSPACE:

                        # remove last character in the string
                        user_text = user_text[:-1]

                    elif event.key == pygame.K_RETURN:

                        active = False

                        if(user_text == password):

                            # break the loop, continue to main code
                            return(True)

                    # displaying the text inside the input box
                    else:

                        user_text += event.unicode

        # it will set background color of screen
        screen.fill((229, 229, 203))

        if active:

            color = color_active

        else:

            color = color_passive

        # draw rectangle
        pygame.draw.rect(screen, color, input_rect)

        text_surface = font.render(user_text, True, (229, 229, 203))

        # render text at given position
        screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))

        # keep increasing width of textfield if user types too much
        input_rect.w = max(300, text_surface.get_width()+10)

        pygame.display.flip()

        # setting fps to 60
        clock.tick(60)
