import pygame as pg
from pygame.locals import *


class ChatInputClass:
    def __init__(self, font_size=20, max_chars=50):
        self.font_size = font_size
        self.max_chars = max_chars
        self.font = pg.font.Font(None, self.font_size)
        self.text = ""
        self.active = False

    def draw(self, screen):
        color = (255, 255, 255)  # White color for the text
        if self.active:
            text_surface = self.font.render("> " + self.text, True, color)
            screen.blit(text_surface, (10, screen.get_height() - 40))

    def handle_event(self, event):
        if event.type == KEYDOWN:
            if event.key == K_RETURN:
                # Process the chat input when the Enter key is pressed
                print("Chat input: " + self.text)
                self.text = ""
                self.active = False
            elif event.key == K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                # Add the character to the chat input if it's not full
                if len(self.text) < self.max_chars:
                    self.text += event.unicode
