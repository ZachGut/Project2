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
        Method to decide the final roll, set its display, and call to adjust the balance.
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
        elif roll <= 2.5:  # 1.5%
            result = [shapes["diamond"]] * 3
            payout_multiplier = 12
        elif roll <= 4:  # 1.5%
            result = [shapes["circle"]] * 3
            payout_multiplier = 9
        elif roll <= 6:  # 2%
            result = [shapes["square"]] * 3
            payout_multiplier = 6
        elif roll <= 8:  # 2%
            result = [shapes["triangle"]] * 3
            payout_multiplier = 4
        elif roll <= 10:  # 2%
            result = [shapes["heart"]] * 3
            payout_multiplier = 3
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
        else:
            result = random.sample(range(6), 3)  # 60%
            payout_multiplier = 0

        self.gui.slot1.config(image=self.gui.shape_images[result[0]])
        self.gui.slot2.config(image=self.gui.shape_images[result[1]])
        self.gui.slot3.config(image=self.gui.shape_images[result[2]])
        self.adjust_balance(payout_multiplier)

    def adjust_balance(self, payout_multiplier: int) -> None:
        """
        Method to adjust the balance based on the bet and roll.
        :param payout_multiplier: The number to multiply the bet with to get the winnings.
        :return: None
        """
        bet = self.gui.current_bet
        winnings = bet * payout_multiplier
        self.gui.balance = self.gui.balance - bet + winnings
        self.gui.label_balance_number.config(text=f'{self.gui.balance}')
