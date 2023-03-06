import pygame
from pygame import mixer as mObject

class soundClass:
    def __init__(self, soundFile=None, mixer=None):
        """
        Ses dosyasını çalıştırmak için yazılmıştır.
        Ses dosyasının yoluna ve pygame mixer sınıfına ihtiyaç duymaktadır.
        mixer sınıfı altındaki Sound sınıfını kullanmakta.
        :param soundFile:
        :param mixer:
        """
        self.__mixer = mixer
        self.__mixer.set_num_channels(50)
        self.__soundFile = soundFile

    def setMixer(self, mixer):
        self.__mixer = mixer
        self.__mixer.set_num_channels(50)

    def setSoundFile(self, soundFile):
        self.__soundFile = soundFile

    def playSound(self):
        """
        mixer sınıfı altındaki Sound sınıfını kullanarak sınıfa gönderilen dosya yolundaki wav ses dosyasını çalıştırır.
        :return: None
        """
        sound = mObject.Sound(self.__soundFile)
        sound.play(0, 1000)


if __name__ == '__main__':
    print('mixer testi 123')
    pygame.init()
    mix = soundClass(mixer=mObject)
    mix.setSoundFile(f'yol/sesdosyasi.wav')
    mix.playSound()
