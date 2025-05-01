from tkinter import *
from logic import *
from PIL import ImageTk, Image
#https://pillow.readthedocs.io/en/stable/handbook/tutorial.html

class Gui:
    """
    A class representing a GUI object.
    """
    def __init__(self, window, logic) -> None:
        """
        Method to set default values and initialize the GUI.
        :param window: The GUI window.
        :param logic: The logic to use.
        :return: None
        """
        self.window = window
        self.logic = logic
        self.balance = 1000
        self.current_bet = 0
        self.load_images()
        self.shape_images = {
            0: self.img_star,
            1: self.img_diamond,
            2: self.img_circle,
            3: self.img_square,
            4: self.img_triangle,
            5: self.img_heart
        }

        self.frame_one = Frame(self.window)
        self.label_balance = Label(self.frame_one, text="Balance: ", font=("Arial", 14))
        self.label_balance_number = Label(
        self.frame_one, text=f'{self.balance}', font=("Arial", 14), bg="white", width=10, relief="sunken")
        self.label_balance.pack(side='left')
        self.label_balance_number.pack(side='left', padx=5)
        self.frame_one.pack(pady=10)

        self.frame_two = Frame(self.window)
        self.slot1 = Label(self.frame_two, image=self.img_blank, borderwidth=4, relief="ridge")
        self.slot2 = Label(self.frame_two, image=self.img_blank, borderwidth=4, relief="ridge")
        self.slot3 = Label(self.frame_two, image=self.img_blank, borderwidth=4, relief="ridge")
        self.slot1.pack(side="left", padx=10)
        self.slot2.pack(side="left", padx=10)
        self.slot3.pack(side="left", padx=10)
        self.frame_two.pack(pady=10)

        self.frame_three = Frame(self.window)
        self.label_bet = Label(self.frame_three, text="Bet: ")
        self.input_bet = Entry(self.frame_three, width=20)
        self.label_bet.pack(side='left')
        self.input_bet.pack(side='right')
        self.frame_three.pack(pady=10)

        self.frame_four = Frame(self.window)
        self.label_instructions = Label(self.frame_four, text="") #Displays instructions and winnings in text format
        self.label_instructions.pack()
        self.frame_four.pack()

        self.frame_five = Frame(self.window)
        self.img_save = ImageTk.PhotoImage(Image.open("images/button.png").resize((100, 100)))
        self.save_button = Button(self.frame_five, image=self.img_save, command=self.submit, borderwidth=0)
        self.save_button.image = self.img_save
        self.save_button.pack()
        self.frame_five.pack(padx=15, pady=15)

        self.frame_six = Frame(self.window)
        self.label_payout = Label(self.frame_six, image=self.img_payout_table)
        self.label_payout.image = self.img_payout_table
        self.label_payout.pack()
        self.frame_six.pack(pady=5)

        self.frame_seven = Frame(self.window)
        self.reset_button = Button(self.frame_seven, text="Reset", command=self.reset, borderwidth=0)
        self.reset_button.pack()
        self.frame_seven.pack(pady=5)

    def load_images(self) -> None:
        """
        Method to load the images for the GUI.
        :return: None
        """
        self.img_blank = ImageTk.PhotoImage(Image.open("images/blank.png").resize((100, 100)))
        self.img_square = ImageTk.PhotoImage(Image.open("images/square.png").resize((100, 100)))
        self.img_circle = ImageTk.PhotoImage(Image.open("images/circle.png").resize((100, 100)))
        self.img_star = ImageTk.PhotoImage(Image.open("images/star.png").resize((100, 100)))
        self.img_diamond = ImageTk.PhotoImage(Image.open("images/diamond.png").resize((100, 100)))
        self.img_heart = ImageTk.PhotoImage(Image.open("images/heart.png").resize((100, 100)))
        self.img_triangle = ImageTk.PhotoImage(Image.open("images/triangle.png").resize((100, 100)))
        self.img_payout_table = ImageTk.PhotoImage(Image.open("images/payout_table.png").resize((200, 300))) #300, 500 for larger screens
        self.img_save = ImageTk.PhotoImage(Image.open("images/button.png").resize((100, 100)))

    def submit(self) -> None:
        """
        Method to send the button press to logic.
        :return: None
        """
        self.logic.submit()

    def reset(self) -> None:
        """
        Method to send the reset press to logic.
        :return: None
        """
        self.logic.reset()
