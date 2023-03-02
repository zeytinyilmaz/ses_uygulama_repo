import pygame as py
import piano_lists as pl
from pygame import mixer

class pygameManegement:
    def __init__(self, pygame=None, mixer=None, notasClass = None):
        self.__pygame = pygame
        self.__mixer = mixer
        self.__notasClass = notasClass

    def setPygameObject(self, pygame):
        self.__pygame = pygame

    def getPygameObject(self):
        return self.__pygame

    def setMixer(self, mixer):
        self.__mixer = mixer

    def getMixer(self):
        return self.__mixer

    def setNotasClass(self, notasClass):
        self.__notasClass = notasClass

    def getNotasClass(self):
        return self.__notasClass

    def getPygameTimer(self):
        if self.__pygame is not None:
            return self.__pygame.time.Clock()
        else:
            raise ModuleNotFoundError('Modül sisteme henüz yüklenmemiş. Önce yüklenmelidir.')

