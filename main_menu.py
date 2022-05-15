from typingTest import *
import sys
import pygame
from pygame.locals import *


def draw_text(screen, msg, y, fsize, color):
    font = pygame.font.Font(None, fsize)
    text = font.render(msg, 1, color)
    text_rect = text.get_rect(center=(1000 / 2, y))
    screen.blit(text, text_rect)
    pygame.display.update()

def main_menu():
    color = (124, 91, 86)

    pygame.init()
    screen = pygame.display.set_mode((1000, 750))
    pygame.display.set_caption('Type Tester')

    screen.fill((255, 255, 255))

    msg = "Type Tester"
    draw_text(screen, msg, 100, 100, color)
    draw_text(screen, "Free-type", 250, 60, color)
    draw_text(screen, "15 seconds", 350, 60, color)
    draw_text(screen, "30 seconds", 450, 60, color)
    draw_text(screen, "60 seconds", 550, 60, color)

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONUP:
                x, y = pygame.mouse.get_pos()
                if 350 <= x <= 650 and 225 <= y <= 275:
                    # print('free type call')
                    game = Game()
                    game.run()
                elif 350 <= x <= 650 and 325 <= y <= 375:
                    print('15 seconds call')
                    # call 15 second type test
                    # change next line once implemented
                    pass
                elif 350 <= x <= 650 and 425 <= y <= 475:
                    print('30 seconds call')
                    # call 15 second type test
                    # change next line once implemented
                    pass
                elif 350 <= x <= 650 and 525 <= y <= 575:
                    print('60 seconds call')
                    # call 15 second type test
                    # change next line once implemented
                    pass

        pygame.display.update()

    #
    # # just some demo data for you to type
    # # data = cycle(['This is an example.', 'This is another, longer sentence.'])
    # infile = open('sentences.txt', 'r')
    # text = []
    # for line in infile:
    #     line = line.rstrip()
    #     text.append(line)
    # infile.close()
    #
    # data = cycle(text)
    # current = next(data)
    # current_idx = 0  # points to the current letter, as you have already guessed
    # correct, total_chars, total_typed = 0, 0, 0
    #
    # font = pygame.freetype.Font(None, 50)
    # # the font in the new freetype module have an origin property.
    # # if you set this to True, the render functions take the dest position
    # # to be that of the text origin, as opposed to the top-left corner
    # # of the bounding box
    # font.origin = True
    # font_height = font.get_sized_height()
    #
    # # we want to know how much space each letter takes during rendering.
    # # the item at index 4 is the 'horizontal_advance_x'
    # M_ADV_X = 4
    #
    # # let's calculate how big the entire line of text is
    # text_surf_rect = font.get_rect(current)
    # # in this rect, the y property is the baseline
    # # we use since we use the origin mode
    # baseline = text_surf_rect.y
    # # now let's create a surface to render the text on
    # # and center it on the screen
    # text_surf = pygame.Surface(text_surf_rect.size)
    # text_surf_rect.center = screen.get_rect().center
    # # calculate the width (and other stuff) for each letter of the text
    # metrics = font.get_metrics(current)
    #
    # start_time = time.time()
    # continue_game = True
    # while continue_game:
    #     clock = pygame.time.Clock()
    #     events = pygame.event.get()
    #     for e in events:
    #         if e.type == pygame.QUIT:
    #             continue_game = False
    #         if e.type == pygame.KEYDOWN:
    #             total_typed += 1
    #             if e.key == pygame.K_LSHIFT or e.key == pygame.K_RSHIFT:
    #                 total_typed -= 1
    #             elif e.unicode == current[current_idx]:
    #                 # if we press the correct letter, move the index
    #                 current_idx += 1
    #                 correct += 1
    #                 if current_idx >= len(current):
    #                     total_chars += len(current)
    #                     # if the sentence is complete, let's prepare the
    #                     # next surface
    #                     current_idx = 0
    #                     current = next(data)
    #                     text_surf_rect = font.get_rect(current)
    #                     baseline = text_surf_rect.y
    #                     text_surf = pygame.Surface(text_surf_rect.size)
    #                     text_surf_rect.center = screen.get_rect().center
    #                     metrics = font.get_metrics(current)
    #
    #                     # calculate total time
    #                     total_time = time.time() - start_time
    #
    #                     # calculate accuracy
    #                     accuracy = (correct - (total_typed - correct)) / total_chars * 100
    #
    #                     # calculate words per minute
    #                     wpm = total_typed * 60 / (5 * total_time)
    #
    #                     message = 'Time: ' + str(round(total_time)) + " secs        Accuracy: " + str(
    #                         round(accuracy)) + '%         Wpm: ' + str(round(wpm))
    #
    #                     print(message)
    #
    #                     # continue_game = False
    #
    #     # clear everything
    #     # screen.fill((255, 237, 225))
    #     # text_surf.fill((255, 237, 225))
    #     screen.fill((255, 255, 255))
    #     text_surf.fill((255, 255, 255))
    #
    #     x = 0
    #     # render each letter of the current sentence one by one
    #     for (idx, (letter, metric)) in enumerate(zip(current, metrics)):
    #         # select the right color
    #         if idx == current_idx:
    #             color = (219, 101, 81)
    #         elif idx < current_idx:
    #             color = (233, 170, 154)
    #         else:
    #             color = (124, 91, 86)
    #         # render the single letter
    #         font.render_to(text_surf, (x, baseline), letter, color)
    #         # and move the start position
    #         x += metric[M_ADV_X]
    #
    #     screen.blit(text_surf, text_surf_rect)
    #     pygame.display.flip()
    #
    # clock.tick(60)


if __name__ == '__main__':
    main_menu()
