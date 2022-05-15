import pygame
from pygame.locals import *
import sys
import time
import random
from itertools import cycle

# 750 x 500

class Game:

    def __init__(self):
        self.w = 1000
        self.h = 750
        self.reset = True
        self.active = False
        self.input_text = ''
        self.word = ''
        self.time_start = 0
        self.total_time = 0
        self.total_typed = 0
        self.accuracy = '0%'
        self.results = 'Time: 0 secs        Accuracy: 0%        wpm: 0'
        self.wpm = 0
        self.end = False
        self.HEAD_C = (124, 91, 86)
        self.TEXT_C = (75, 85, 58)
        self.RESULT_C = (219, 101, 81)
        self.RECT_C = (189, 154, 130)
        self.RESET_C = (124, 91, 86)
        self.previous = ''
        self.data = ''

        pygame.init()

        self.screen = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption('Type Tester')

    def draw_text(self, screen, msg, y, fsize, color):
        font = pygame.font.Font(None, fsize)
        text = font.render(msg, 1, color)
        text_rect = text.get_rect(center=(self.w / 2, y))
        screen.blit(text, text_rect)
        pygame.display.update()

    def open_sentences(self):
        infile = open('sentences.txt', 'r')
        text = []
        for line in infile:
            line = line.rstrip()
            text.append(line)
        infile.close()
        self.data = cycle(text)

    def get_sentence(self):
        return next(self.data)

    def show_results(self, screen):
        if not self.end:
            # Calculate time
            self.total_time = time.time() - self.time_start

            # Calculate accuracy
            count = 0
            for i, c in enumerate(self.word):
                try:
                    if self.input_text[i] == c:
                        count += 1
                except:
                    pass
            self.accuracy = (count - (self.total_typed - count)) / len(self.word) * 100
            if self.accuracy < 0:
                self.accuracy = 0

            # Calculate words per minute
            self.wpm = len(self.input_text) * 60 / (5 * self.total_time)
            self.end = True

            self.results = 'Time: ' + str(round(self.total_time)) + " secs      Accuracy: " + str(
                round(self.accuracy)) + '%      wpm: ' + str(round(self.wpm))

            self.draw_text(screen, "Reset", self.h - 70, 30, self.RESET_C)

            pygame.display.update()

    def run(self):
        self.open_sentences()
        self.reset_game()

        self.active = True
        self.input_text = ''

        self.running = True
        while (self.running):
            clock = pygame.time.Clock()
            self.screen.fill((255, 255, 255), (50, 345, 900, 75))
            pygame.draw.rect(self.screen, self.RECT_C, (50, 345, 900, 75), 3)
            # update the text of user input
            self.draw_text(self.screen, self.input_text, 382, 30, self.RECT_C)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                    sys.exit()

                elif event.type == pygame.MOUSEBUTTONUP:
                    x, y = pygame.mouse.get_pos()
                    if 310 <= x <= 510 and y >= 600 and self.end:
                        self.reset_game()
                        x, y = pygame.mouse.get_pos()

                elif event.type == pygame.KEYDOWN:
                    if self.active and not self.end:
                        self.total_typed += 1
                        if event.key == pygame.K_RETURN:
                            self.total_typed -= 1
                            self.show_results(self.screen)
                            self.draw_text(self.screen, self.results, self.h - 200, 36, self.RESULT_C)
                            self.end = True

                        elif event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                            self.total_typed -= 1

                        elif event.key == pygame.K_BACKSPACE:
                            self.input_text = self.input_text[:-1]
                        else:
                            try:
                                self.input_text += event.unicode
                            except:
                                pass

            pygame.display.update()

        clock.tick(60)

    def reset_game(self):
        self.reset = False
        self.end = False

        self.input_text = ''
        self.word = ''
        self.time_start = 0
        self.total_time = 0
        self.total_typed = 0
        self.wpm = 0

        # Get next sentence
        self.word = self.get_sentence()
        if not self.word:
            self.reset_game()
        # drawing heading
        self.screen.fill((255, 255, 255))
        msg = "Type Tester"
        self.draw_text(self.screen, msg, 80, 80, self.HEAD_C)
        # draw the rectangle for input box
        pygame.draw.rect(self.screen, self.RECT_C, (50, 345, 900, 75), 3)

        # draw the sentence string
        self.draw_text(self.screen, self.word, 275, 40, self.TEXT_C)

        self.time_start = time.time()

        pygame.display.update()

if __name__ == '__main__':
    Game().run()
