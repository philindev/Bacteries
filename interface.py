import pygame


class Interface:
    @staticmethod
    def icon(w, h, url):
        icon = pygame.image.load(url)
        icon = pygame.transform.scale(icon, (w, h))
        return icon




