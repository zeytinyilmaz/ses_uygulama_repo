
class soundNames:
    def __init__(self):
        self.__whiteButtons = [
            'A0', 'B0', 'C1', 'D1', 'E1', 'F1', 'G1',
            'A1', 'B1', 'C2', 'D2', 'E2', 'F2', 'G2',
            'A2', 'B2', 'C3', 'D3', 'E3', 'F3', 'G3',
            'A3', 'B3', 'C4', 'D4', 'E4', 'F4', 'G4',
            'A4', 'B4', 'C5', 'D5', 'E5', 'F5', 'G5',
            'A5', 'B5', 'C6', 'D6', 'E6', 'F6', 'G6',
            'A6', 'B6', 'C7', 'D7', 'E7', 'F7', 'G7',
            'A7', 'B7', 'C8'
        ]
        self.__black_notes = [
            'Bb0', 'Db1', 'Eb1', 'Gb1', 'Ab1',
            'Bb1', 'Db2', 'Eb2', 'Gb2', 'Ab2',
            'Bb2', 'Db3', 'Eb3', 'Gb3', 'Ab3',
            'Bb3', 'Db4', 'Eb4', 'Gb4', 'Ab4',
            'Bb4', 'Db5', 'Eb5', 'Gb5', 'Ab5',
            'Bb5', 'Db6', 'Eb6', 'Gb6', 'Ab6',
            'Bb6', 'Db7', 'Eb7', 'Gb7', 'Ab7',
            'Bb7'
        ]

    def getwhiteButtonNotas(self):
        return self.__whiteButtons

    def getBlackButtonNotas(self):
        return self.__black_notes