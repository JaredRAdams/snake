from gui import Gui
import time

def main():
    gui = Gui()
    width = gui.get_width()
    height = gui.get_height()
    try:
        continuePlaying = True
        x=0
        while continuePlaying:
            c = gui.get_keypress()
            if c != "":
                continuePlaying = False

            #draw on the screen
            gui.clear()
            gui.draw_text("Hello", 15, x , "RED", "GREEN")
            gui.draw_text("The Joke", x,15,"RED","GREEN")
            gui.refresh()
            x += 1
            #slow the computer down
            time.sleep(0.1)

    except Exception as e:
        gui.quit()
        print (e)
        return

    gui.quit()    #quit gracefully

if __name__ == "__main__":
    main()
    
