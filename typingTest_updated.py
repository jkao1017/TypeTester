# Authors: Gabrielle David, Jonathan Kao
# How to run Typing Tester:
#   Run program from typingTest.py
#   The main menu will have 4 options:
#       1. Free-type
#       2. 15 seconds
#       3. 30 seconds
#       4. 60 seconds
#   When clicking each of these options by using the
#   mouse, the player will be redirected to each
#   corresponding typing test.
#   1. Free-type:
#       A prompt will be shown on the screen, and
#       the player must type the prompt as fast as
#       they can. When the player hits the "Return" key,
#       the time taken to type the prompt, accuracy,
#       and words per minute are displayed on screen.
#       The player can choose to restart and receive
#       a new typing test prompt, or they can return
#       to the main menu by pressing the Main Menu button.
#   2. 15 seconds, 30 seconds, 60 seconds:
#       Two lines of text are displayed on the screen, and
#       the player must type each letter correctly before
#       they can type the next. After the player correctly
#       types 2 lines, a new line of words will display,
#       and the first line will disappear. The timer starts
#       once the player starts typing, and the time
#       remaining is displayed on the screen. Once the time is up,
#       the words per minute are displayed on the screen.
#       The player can return to the Main Menu to restart
#       the game or try another typing test.
import time
from itertools import cycle
import sys
from pygame.locals import *
import pygame
import pygame.freetype
import random


def draw_text(screen, msg, y, fsize, color):
    font = pygame.font.Font(None, fsize)
    text = font.render(msg, 1, color)
    text_rect = text.get_rect(center=(1000 / 2, y))
    screen.blit(text, text_rect)


def draw_menu_text(screen, msg, y, fsize, color):
    font = pygame.font.Font(None, fsize)
    text = font.render(msg, 1, color)
    text_rect = text.get_rect(topleft=(25, y))
    screen.blit(text, text_rect)



def main_menu():
    color = (124, 91, 86)

    pygame.init()
    screen = pygame.display.set_mode((1000, 750))
    pygame.display.set_caption('Type Tester')

    screen.fill((255, 237, 225))

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

                    main(15)

                elif 350 <= x <= 650 and 425 <= y <= 475:

                    main(30)
                    pass
                elif 350 <= x <= 650 and 525 <= y <= 575:

                    main(60)


        pygame.display.update()

def initialize(current, font, screen):
    text_surf_rect = []
    baseline = []
    text_surf = []
    metrics = []

    for i in range(len(current)):
        text_surf_rect.append(font.get_rect(current[i]))
        metrics.append(font.get_metrics(current[i]))

    for i in range(len(text_surf_rect)):
        baseline.append(text_surf_rect[i].y)
        text_surf.append(pygame.Surface(text_surf_rect[i].size))
        text_surf_rect[i].left = screen.get_rect().left + (screen.get_rect().width / 10)

    return text_surf_rect, baseline, text_surf, metrics


def render_sentence(current, baseline, text_surf, font, metrics, x, index, sentence1, M_ADV_X):
    for (idx, (letter, metric)) in enumerate(zip(current[index], metrics[index])):
        if index == 0:
            if sentence1:
                color = 'white'
            else:
                color = (75,85,58)
        else:
            color = (75,85,58)
        # render the single letter
        font.render_to(text_surf[index], (x, baseline[index]), letter, color)
        # and move the start position
        x += metric[M_ADV_X]


def generate_word_bank():
    infile = open('common_words.txt', 'r')

    word_bank = []
    for line in infile:
        line = line.rstrip()
        word_bank.append(line)
    infile.close()
    return word_bank


def generate_sentences(word_bank):
    sentence = ""
    while len(sentence) + 10 < 55:
        sentence = sentence + random.choice(word_bank) + " "
    return sentence


def main(seconds):
    pygame.init()
    screen = pygame.display.set_mode((1000, 750))
    is_start = True

    count = 0

    word_bank = generate_word_bank()
    sentence = generate_sentences(word_bank)
    timer = pygame.USEREVENT + 1
    timer_sec = seconds

    timer_font = pygame.font.Font(None, 38)
    if seconds == 15:
        timer_text = timer_font.render("00:15", True, (243, 131, 115))
    elif seconds == 30:
        timer_text = timer_font.render("00:30", True, (243, 131, 115))
    else:
        timer_text = timer_font.render("01:00", True, (243, 131, 115))
    current = [generate_sentences(word_bank), generate_sentences(word_bank), generate_sentences(word_bank)]
    current_idx = 0  # points to the current letter, as you have already guessed

    font = pygame.freetype.Font(None, 30)
    # the font in the new freetype module have an origin property.
    # if you set this to True, the render functions take the dest position
    # to be that of the text origin, as opposed to the top-left corner
    # of the bounding box
    font.origin = True
    font_height = font.get_sized_height()

    # we want to know how much space each letter takes during rendering.
    # the item at index 4 is the 'horizontal_advance_x'
    M_ADV_X = 4
    is_sentence1 = False

    text_surf_rect, baseline, text_surf, metrics = initialize(current, font, screen)
    i = 0
    isRunning = True
    while isRunning:
        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                sys.exit()
            if e.type == pygame.MOUSEBUTTONUP:
                x, y = pygame.mouse.get_pos()
                if 0 <= x <= 150 and 0 <= y <= 50:
                    pygame.time.set_timer(timer, 0)
                    main_menu()
                if 450 <= x <= 550 and y >= 600:
                    pygame.time.set_timer(timer,0)
                    main(seconds)

            if e.type == pygame.KEYDOWN:

                if is_start:
                    pygame.time.set_timer(timer, 1000)
                    is_start = False

                if timer_sec > 0:
                    if e.unicode == current[i][current_idx].lower():
                        # if we press the correct letter, move the index
                        current_idx += 1
                        count += 1
                        if current_idx >= len(current[i]):

                            if i == 0:
                                is_sentence1 = True
                            elif i == 1:

                                current.pop(0)
                                current.append(sentence)
                                text_surf_rect, baseline, text_surf, metrics = initialize(current, font, screen)
                                sentence = generate_sentences(word_bank)

                            i = 1
                            current_idx = 0

            if e.type == timer:
                if timer_sec > 0:
                    timer_sec -= 1
                    timer_text = timer_font.render("00:%02d" % timer_sec, True, (243, 131, 115))

        # clear everything
        screen.fill((255, 237, 225))
        for z in range(len(current)):
            text_surf[z].fill((255, 237, 225))

        x = 0
        render_sentence(current, baseline, text_surf, font, metrics, x, 0, is_sentence1, M_ADV_X)
        render_sentence(current, baseline, text_surf, font, metrics, x, 1, is_sentence1, M_ADV_X)
        render_sentence(current, baseline, text_surf, font, metrics, x, 2, is_sentence1, M_ADV_X)

        for (idx, (letter, metric)) in enumerate(zip(current[i], metrics[i])):

            # select the right color
            if idx == current_idx:
                color = (184, 115, 104)
            elif idx < current_idx:
                color = 'white'
            else:
                color = (75,85,58)
            # render the single letter
            font.render_to(text_surf[i], (x, baseline[i]), letter, color)
            # and move the start position
            x += metric[M_ADV_X]

        if timer_sec == 0:
            wpm = 0
            if seconds == 15:
                wpm = (count / 5) * 4
            elif seconds == 30:
                wpm = (count / 5) * 2
            else:
                wpm = (count/5)
            wpm_text = timer_font.render('Words Per Minute: ' + str(wpm), True, (219, 101, 81))
            screen.blit(wpm_text, (350, 400))

        screen.blit(text_surf[0], (text_surf_rect[0].x + 50, text_surf_rect[0].y + 180))
        screen.blit(text_surf[1], (text_surf_rect[1].x + 50, text_surf_rect[1].y + 240))
        screen.blit(text_surf[2], (text_surf_rect[2].x + 50, text_surf_rect[2].y + 300))
        screen.blit(timer_text, (text_surf_rect[0].x + 50, 400))
        draw_text(screen, 'Type Tester', 80, 80, (124, 91, 86))
        draw_text(screen, "Reset", 650, 30, (124, 91, 86))
        draw_menu_text(screen, 'Main Menu', 25, 30, (124, 91, 86))

        pygame.display.flip()



class Game:

    def __init__(self):
        self.w = 1000
        self.h = 750
        self.reset = True
        self.active = False
        self.is_start = False
        self.input_text = ''
        self.word = ''
        self.time_start = 0
        self.end_time = 0
        self.total_time = 0
        self.total_typed = 0
        self.accuracy = 0
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

    def draw_menu_text(self, screen, msg, y, fsize, color):
        font = pygame.font.Font(None, fsize)
        text = font.render(msg, 1, color)
        text_rect = text.get_rect(topleft=(25, y))
        screen.blit(text, text_rect)
        pygame.display.update()

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
            self.total_time = self.end_time - self.time_start

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
        while self.running:
            clock = pygame.time.Clock()
            self.screen.fill((255, 237, 225), (50, 345, 900, 75))
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
                    if 0 <= x <= 150 and 0 <= y <= 50:


                        main_menu()

                    if 310 <= x <= 510 and y >= 600 and self.end:
                        self.reset_game()
                        x, y = pygame.mouse.get_pos()

                elif event.type == pygame.KEYDOWN:
                    if self.is_start:
                        self.time_start = time.time()
                        self.is_start = False
                    if self.active and not self.end:
                        self.total_typed += 1
                        if event.key == pygame.K_RETURN:
                            self.end_time = time.time()
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
        self.is_start = True

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
        self.screen.fill((255, 237, 225))
        msg = "Type Tester"
        self.draw_text(self.screen, msg, 80, 80, self.HEAD_C)
        self.draw_menu_text(self.screen, "Main Menu", 25, 30, self.HEAD_C)
        # draw the rectangle for input box
        pygame.draw.rect(self.screen, self.RECT_C, (50, 345, 900, 75), 3)

        # draw the sentence string
        self.draw_text(self.screen, self.word, 275, 40, self.TEXT_C)

        pygame.display.update()


if __name__ == '__main__':
    main_menu()

