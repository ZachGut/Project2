from gui import *
import random
#https://docs.python.org/3/library/random.html

class Logic:
    """
    A class representing the logic for the GUI.
    """
    def __init__(self, gui) -> None:
        """
        Method to initialize the GUI.
        :param gui: The GUI.
        :return: None
        """
        self.gui = gui

    def submit(self) -> None:
        """
        Method to check valid bet and roll the slots.
        :return: None
        """
        try:
            bet = int(self.gui.input_bet.get())
            if bet <= 0:
                raise ValueError
            if bet > self.gui.balance:
                raise ValueError
            self.gui.label_instructions.config(text="")
            self.gui.input_bet.config(state="disabled")
            self.gui.save_button.config(state="disabled")
            self.gui.reset_button.config(state="disabled")
            self.gui.current_bet = bet
            self.roll()
        except ValueError:
            self.gui.label_instructions.config(text="Enter a valid bet value")

    def reset(self) -> None:
        """
        Method to reset the GUI.
        :return: None
        """
        self.gui.label_instructions.config(text="")
        self.gui.balance = 1000
        self.gui.label_balance_number.config(text=f'{self.gui.balance}')
        self.gui.slot1.config(image=self.gui.img_blank)
        self.gui.slot2.config(image=self.gui.img_blank)
        self.gui.slot3.config(image=self.gui.img_blank)
        self.gui.input_bet.delete(0, END)
        self.gui.window.focus_set()

    def roll(self) -> None:
        """
        Method to initialize the roll and begin the rolling.
        :return: None
        """
        self.gui.roll_count = 0
        self.gui.sleeptime = 10
        self.animate_roll()

    def animate_roll(self) -> None:
        """
        Method to animate the roll and call the final roll.
        :return: None
        """
        if self.gui.roll_count <= 14:
            rolled_image1 = self.gui.shape_images[random.randint(0, 5)]
            rolled_image2 = self.gui.shape_images[random.randint(0, 5)]
            rolled_image3 = self.gui.shape_images[random.randint(0, 5)]
            self.gui.slot1.config(image=rolled_image1)
            self.gui.slot2.config(image=rolled_image2)
            self.gui.slot3.config(image=rolled_image3)
            self.gui.roll_count += 1
            self.gui.sleeptime += 5
            self.gui.window.after(self.gui.sleeptime, self.animate_roll)
        else:
            self.choose_shapes()
            self.gui.window.after(100, lambda: self.gui.save_button.config(state="normal"))
            self.gui.window.after(100, lambda: self.gui.input_bet.config(state="normal"))
            self.gui.window.after(100, lambda: self.gui.reset_button.config(state="normal"))

    def choose_shapes(self) -> None:
        """
        Method to decide the final roll, set its display, call to adjust the balance, and call to display winnings.
        :return: None
        """
        roll = random.uniform(0, 100)
        shapes = {
            "star": 0,
            "diamond": 1,
            "circle": 2,
            "square": 3,
            "triangle": 4,
            "heart": 5
        }

        if roll <= 1:  # 1%
            result = [shapes["star"]] * 3
            payout_multiplier = 30
            winnings_text = "Stars"
        elif roll <= 2.5:  # 1.5%
            result = [shapes["diamond"]] * 3
            payout_multiplier = 12
            winnings_text = "Diamonds"
        elif roll <= 4:  # 1.5%
            result = [shapes["circle"]] * 3
            payout_multiplier = 9
            winnings_text = "Circles"
        elif roll <= 6:  # 2%
            result = [shapes["square"]] * 3
            payout_multiplier = 6
            winnings_text = "Squares"
        elif roll <= 8:  # 2%
            result = [shapes["triangle"]] * 3
            payout_multiplier = 4
            winnings_text = "Triangles"
        elif roll <= 10:  # 2%
            result = [shapes["heart"]] * 3
            payout_multiplier = 3
            winnings_text = "Hearts"
        elif roll <= 40:  # 30%
            pair_shape = random.randint(0, 5)
            available_shapes = []
            for i in range(6):
                if i != pair_shape:
                    available_shapes.append(i)
            other_shape = random.choice(available_shapes)
            result = [pair_shape, pair_shape, other_shape]
            random.shuffle(result)
            payout_multiplier = 2
            winnings_text = "Pair"
        else:
            result = random.sample(range(6), 3)  # 60%
            payout_multiplier = 0
            winnings_text = "Nothing"

        self.gui.slot1.config(image=self.gui.shape_images[result[0]])
        self.gui.slot2.config(image=self.gui.shape_images[result[1]])
        self.gui.slot3.config(image=self.gui.shape_images[result[2]])

        bet = self.gui.current_bet
        winnings = bet * payout_multiplier
        self.adjust_balance(bet, winnings)

        profit = winnings - bet
        self.display_winnings(profit, winnings_text)

    def adjust_balance(self, bet: int, winnings: int) -> None:
        """
        Method to adjust the balance based on the bet and roll.
        :param bet: The amount of the bet.
        :param winnings: The bet times the payout multiplier.
        :return: None
        """
        self.gui.balance = self.gui.balance - bet + winnings
        self.gui.label_balance_number.config(text=f'{self.gui.balance}')

    def display_winnings(self, profit: int, winnings_text: str) -> None:
        """
        Method to display the winnings in text format.
        This method was added as feedback from the instructor.
        :param profit: The winnings minus the initial bet.
        :param winnings_text: The text to display.
        :return: None
        """
        if winnings_text == "Pair":
            self.gui.label_instructions.config(text=f'You made {profit} profit with a {winnings_text} of shapes.')
        elif winnings_text == "Nothing":
            self.gui.label_instructions.config(text=f'You lost {profit * -1} money with no matching shapes.')
        else:
            self.gui.label_instructions.config(text=f'You made {profit} profit with 3 {winnings_text}.')
