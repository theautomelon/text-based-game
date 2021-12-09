from pygame import mixer


def playMusic():
    mixer.init()
    mixer.music.load('music/bensound-thejazzpiano.mp3')
    mixer.music.play(-1)

