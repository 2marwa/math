from tkinter import *
import random
from tkinter import messagebox

class MathGame:
    def __init__(self, master):
        self.master = master
        master.title("Math Game")
        master.configure(borderwidth=10, relief='ridge', bg="#F9C7BE")
        master.geometry("1000x700") #w h

        self.welcome_screen()
        
    def welcome_screen(self):
        # Create a frame for the welcome screen
        self.welcome_frame = Frame(self.master, bg="#F9C7BE")
        self.welcome_frame.pack(fill=BOTH, expand=True) # Frame will adjust automatically

        # Create difficulty buttons
        label = Label(self.welcome_frame, text="Please select your difficulty level", font=("Helvetica", 16), bg="#F9C7BE")
        label.pack(pady=20)

        button_easy = Button(self.welcome_frame, text="Easy", command=self.run_easy, bg="#CE6A6C", height=6, width=20, fg="white")
        button_easy.pack(pady=10)

        button_medium = Button(self.welcome_frame, text="Medium", command=self.run_medium, bg="#CE6A6C", height=6, width=20, fg="white")
        button_medium.pack(pady=10)

        button_hard = Button(self.welcome_frame, text="Hard", command=self.run_hard, bg="#CE6A6C", height=6, width=20, fg="white")
        button_hard.pack(pady=10)

        button_quit = Button(self.welcome_frame, text="Exit", command=self.close_window, bg="#EDADA3")
        button_quit.pack(pady=100)

    def run_easy(self):
        self.welcome_frame.pack_forget()  # Hide welcome screen
        self.run_easy_level()

    def run_medium(self):
        self.welcome_frame.pack_forget()  # Hide welcome screen
        self.run_medium_level()

    def run_hard(self):
        self.welcome_frame.pack_forget()  # Hide welcome screen
        self.run_hard_level()

    def run_easy_level(self):
        self.create_math_problem("easy")

    def run_medium_level(self):
        self.create_math_problem("medium")

    def run_hard_level(self):
        self.create_math_problem("hard")

    def create_math_problem(self, level):
        # Placeholder for creating math problems according to difficulty level
        print(f"Running {level} level math problem")

    # Exit button
    def close_window(self): 
        self.master.destroy()

root = Tk()
app = MathGame(root)
root.mainloop()
