import pygame


class Interface:
    @staticmethod
    def footer(Surface):
        return pygame.draw.rect(Surface, (255, 255, 255), (0, 580, 960, 60))

    @staticmethod
    def magazine(Surface):
        return pygame.draw.rect(Surface, (255, 100, 40), (840, 0, 120, 640))


    @staticmethod
    def icon(w, h, url):
        icon = pygame.image.load(url)
        icon = pygame.transform.scale(icon, (w, h))
        return icon




