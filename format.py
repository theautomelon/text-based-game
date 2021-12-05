import textwrap
import time

class Format:
    def printFerret(): #ASCII art taken from http://www.ascii-art.de/ascii/def/ferret.txt
        print(",____          (\=-,")
        print("\ '=.`'-.______/ /^")
        print(" `-._.-'(=====' /")
        print("         \<'--\(")
        print("          ^^   ^^")
        
    def printGameTitle():
        print(" ______     ______     ______     __  __        ______   ______     ______   ______     ______        ______   ______     ______     ______     ______     ______  ")
        print("/\  == \   /\  __ \   /\  ___\   /\ \/ /       /\  == \ /\  __ \   /\  == \ /\  ___\   /\  == \      /\  ___\ /\  ___\   /\  == \   /\  == \   /\  ___\   /\__  _\ ")
        print("\ \  __<   \ \ \/\ \  \ \ \____  \ \  _'-.     \ \  _-/ \ \  __ \  \ \  _-/ \ \  __\   \ \  __<      \ \  __\ \ \  __\   \ \  __<   \ \  __<   \ \  __\   \/_/\ \/ ")
        print(" \ \_\ \_\  \ \_____\  \ \_____\  \ \_\ \_\     \ \_\    \ \_\ \_\  \ \_\    \ \_____\  \ \_\ \_\     \ \_\    \ \_____\  \ \_\ \_\  \ \_\ \_\  \ \_____\    \ \_\ ")
        print("  \/_/ /_/   \/_____/   \/_____/   \/_/\/_/      \/_/     \/_/\/_/   \/_/     \/_____/   \/_/ /_/      \/_/     \/_____/   \/_/ /_/   \/_/ /_/   \/_____/     \/_/ ")
        
    def printIntroText():
        introText= "Welcome, you little weasel. You are a ferret, specifically Fabio the Illustrious Ferret. You, in your infinite wisdom, have decided to escape from your human enslavers and embark on a journey to finally make a name for yourself. The road to stardom is arduous but luckily your former masters taught you everything there is to know about the ancient combat ritual 剪刀石頭布, or as the filthy Americans call it- Rock, Paper, Scissors. Stay on your guard, as there is not telling what dangers may lie ahead."
        dedentedText = textwrap.dedent(introText).strip()
        print(dedentedText)
        
    def printDivider(length):
        startAndEndChar = '+'
        midChar = '-'
        divider = startAndEndChar
        for i in range(length-2):
            divider += midChar
        divider += startAndEndChar
        print(divider)
        
    def printScroll(): #scroll taken from https://ascii.co.uk/art/scroll
        sleepTime = 0.75
        print(' .-.---------------------------------.-.')
        time.sleep(sleepTime*0.5)
        print('((o))                                   )')
        time.sleep(sleepTime*0.5)
        print(' \\U/_______          _____         ____/')
        time.sleep(sleepTime*0.5)
        print('   |                                  |')
        time.sleep(sleepTime)
        print('   |    WELCOME, YOU LITTLE WEASEL    |')
        time.sleep(sleepTime)
        print('   |                                  |')
        time.sleep(sleepTime)
        print('   |  You are a ferret, specifically  |')
        time.sleep(sleepTime)
        print('   |   Fabio the Illustrious Ferret   |')
        time.sleep(sleepTime*0.5)
        print('   |                                  |')
        time.sleep(sleepTime)
        print('   |  You, in your infinite wisdom,   |')
        time.sleep(sleepTime)
        print('   |   have decided to escape from    |')
        time.sleep(sleepTime)
        print('   | your human enslavers and embark  |')
        time.sleep(sleepTime)
        print('   |  on a journey to finally make a  |')
        time.sleep(sleepTime)
        print('   |        name for yourself         |')
        time.sleep(sleepTime)
        print('   |                                  |')
        time.sleep(sleepTime*0.5)
        print('   | The road to stardom is arduous,  |')
        time.sleep(sleepTime)
        print('   |  but luckily your former masters |')
        time.sleep(sleepTime)
        print('   | taught you everything there is   |')
        time.sleep(sleepTime)
        print('   |  know about the ancient combat   |')
        time.sleep(sleepTime)
        print('   |   ritual 剪刀石頭布, or as the   |')
        time.sleep(sleepTime)
        print('   |     filthy Americans call it     |')
        time.sleep(sleepTime*0.5)
        print('   |                                  |')
        time.sleep(sleepTime)
        print('   |      ROCK, PAPER, SCISSORS       |')
        time.sleep(sleepTime*0.5)
        print('   |                                  |')
        time.sleep(sleepTime)
        print('   |        Stay on your guard        |')
        time.sleep(sleepTime)
        print('   |      as there is no telling      |')
        time.sleep(sleepTime)
        print('   |           what dangers           |')
        time.sleep(sleepTime)
        print('   |          may lie ahead           |')
        time.sleep(sleepTime*0.5)
        print('   |                                  |')
        time.sleep(sleepTime)
        print('   |             ~GOOD LUCK           |')
        time.sleep(sleepTime*0.5)
        print('   |                                  |')
        time.sleep(sleepTime*0.5)
        print('   |____    _______    __  ____    ___|')
        time.sleep(sleepTime*0.5)
        print('  /A\                                  \\')
        time.sleep(sleepTime*0.5)
        print(' ((o))                                  )')
        time.sleep(sleepTime*0.5)
        print("  '-'----------------------------------'")
        
        