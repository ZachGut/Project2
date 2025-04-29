from gui import Gui, Logic, Tk

"""
(gui.py) Asked AI for assistance on troubleshooting the images not loading which told me how to use the Pillow library to
load the images.
(logic.py) Also self.gui.window.after as I was trying to use the sleep function from the time library
which was freezing my entire gui.
"""

def main() -> None:
    """
    Method to start the application.
    :return: None
    """
    window = Tk()
    window.title("CSCI1620-Project2")
    window.geometry("1000x720") #1100x950 for larger screens
    window.resizable(False, False)
    gui = Gui(window, None)
    logic = Logic(gui)
    gui.logic = logic
    window.mainloop()

if __name__ == '__main__':
    main()
