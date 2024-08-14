from tkinter import *
from tkinter import font
from tkinter import messagebox
import random


class MathGame:
    def __init__(self, master):
        self.master = master
        master.title("Math Game")
        master.configure(borderwidth=10, relief='ridge', bg="#F9C7BE")
        master.geometry("1000x700")  # Width x Height

        self.kfont = ("Kristen ITC")
        self.welcome_screen()

    def welcome_screen(self):
        self.welcome_screen_frame = Frame(self.master, bg="#F9C7BE")
        self.welcome_screen_frame.pack(fill=BOTH, expand=True)  # Frame will adjust automatically

        # Create a label with the welcome message
        welcome_label = Label(self.welcome_screen_frame, text="Welcome to [Game Name] !!", font=(self.kfont, 24), bg="#F9C7BE")
        welcome_label.pack(pady=20)

        name_label = Label(self.welcome_screen_frame, text="Please enter your full name below:", font=(self.kfont, 12), bg="#F9C7BE")
        name_label.pack(pady=10)

        # Entry widget for name input
        self.name_entry = Entry(self.welcome_screen_frame, font=(self.kfont, 12))
        self.name_entry.pack(pady=3, side=TOP)

        if not re.match(r'^[a-zA-Z]+$", self.name_entry): # If the name is not a-z, display error window.
            messagebox.showerror("Please enter your name using letters a-z!") # Clarifying what the error window will say.
            return # Continuing.



        # Create a button to go to the levels screen
        levels_button = Button(self.welcome_screen_frame, text="Levels Page", command=self.show_levels_screen, bg="#CE6A6C", height=2, width=20, fg="white")
        levels_button.pack(pady=3)

        # Exit button
        exit_button = Button(self.welcome_screen_frame, text="Exit", command=self.close_window, bg="#EDADA3", height=2, width=10, fg="white")
        exit_button.pack(side=BOTTOM, anchor=SE, padx=10, pady=10)

    def show_levels_screen(self):
        self.welcome_screen_frame.pack_forget()  # Hide the welcome screen
        self.levels_screen()

    def levels_screen(self):
        self.levels_frame = Frame(self.master, bg="#F9C7BE")
        self.levels_frame.pack(fill=BOTH, expand=True)  # Frame will adjust automatically

        # Create difficulty buttons
        label = Label(self.levels_frame, text="Please select your difficulty level:", font=(self.kfont, 16), bg="#F9C7BE")
        label.pack(pady=20)

        button_easy = Button(self.levels_frame, text="Easy", command=self.run_easy, bg="#CE6A6C", height=6, width=20, fg="white")
        button_easy.pack(pady=10)

        button_medium = Button(self.levels_frame, text="Medium", command=self.run_medium, bg="#CE6A6C", height=6, width=20, fg="white")
        button_medium.pack(pady=10)

        button_hard = Button(self.levels_frame, text="Hard", command=self.run_hard, bg="#CE6A6C", height=6, width=20, fg="white")
        button_hard.pack(pady=10)

        # Exit button
        exit_button = Button(self.levels_frame, text="Exit", command=self.close_window, bg="#EDADA3", height=2, width=10, fg="white")
        exit_button.pack(side=BOTTOM, anchor=SE, padx=10, pady=10)

    def run_easy(self):
        self.levels_frame.pack_forget()  # Hide levels screen
        self.run_easy_level()

    def run_medium(self):
        self.levels_frame.pack_forget()  # Hide levels screen
        self.run_medium_level()

    def run_hard(self):
        self.levels_frame.pack_forget()  # Hide levels screen
        self.run_hard_level()

    def run_easy_level(self):
        self.create_math_problem("easy")

    def run_medium_level(self):
        self.create_math_problem("medium")

    def run_hard_level(self):
        self.create_math_problem("hard")

    def create_math_problem(self, level):
        # actual math stuff here
        pass

    # Exit button
    def close_window(self):
        self.master.destroy()


root = Tk()
app = MathGame(root)
root.mainloop()
