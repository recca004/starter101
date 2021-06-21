import pyautogui as pt

from time import sleep


# red heart colour =(237,73,86)

class GuiCommands:
    def __init__(self, x,y):
        self.x=x
        self.y=y

    def navigate_to_hear(self,speed):
        position=pt.locateOnScreen("bookmark.png", confidence=0.7)
        self.x=position[0]-550
        self.y=position[1]+10
        pt.moveTo(self.x,self.y, duration=speed)
        print("Navigating to heart!")
        sleep(.3)

commands=GuiCommands(0,0)
for i in range(5):
    try:
        commands.navigate_to_hear(1)
        if pt.pixelMathchesColor(pt.position().x,pt.position().y, (255, 255, 255),tolerance=10):
            pt.scroll(5000)
            sleep(.3)
        else:
            pt.click()
            sleep(.3)

    except Exception as e:
        print(e)
        pt.scroll(5000)
        sleep(.3)