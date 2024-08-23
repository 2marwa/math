from tkinter import *
import re
import random
from tkinter import messagebox
from PIL import Image, ImageTk # pip install Pillow
import requests # pip install requests
import os
class MathGame:
    def __init__(self, master):

        
        # Main window
        self.master = master
        master.title("Math Game")  
        master.configure(borderwidth=10, relief='ridge', bg="#F9C7BE")
        master.geometry("800x600")  # Window size


        self.kfont = ("Kristen ITC")  
        self.current_question = 0  # Track the current question number
        self.correct_answers = 0  # Track the number of correct answers
        self.total_questions = 7  # Define the total number of questions
        self.score = 0  # Initialize the score
        self.player_name = None  # Initialize the player's name

        
        # Load GIF
        self.gif_path = os.path.join(os.path.dirname(__file__), "waddle jump.gif")
        self.load_gif()

        self.character_selection()

    def load_gif(self):
        try:
            self.waddle_gif_path = os.path.join(os.path.dirname(__file__), "waddle jump.gif")
            openImage = Image.open(self.waddle_gif_path)
            frames = openImage.n_frames
            self.waddle_images = [PhotoImage(file=self.waddle_gif_path, format=f"gif -index {i}") for i in range(frames)]

            self.kirby_gif_path = os.path.join(os.path.dirname(__file__), "kirby jump.gif")
            openImage = Image.open(self.kirby_gif_path)
            frames = openImage.n_frames
            self.kirby_images = [PhotoImage(file=self.kirby_gif_path, format=f"gif -index {i}") for i in range(frames)]
        except Exception as e:
            print(f"Error loading GIF: {e}")


    def animate_gif(self):
        if hasattr(self, 'waddle_gif_label') and self.waddle_gif_label:
            self.current_waddle_frame = 0
        if hasattr(self, 'kirby_gif_label') and self.kirby_gif_label:
            self.current_kirby_frame = 0
        self.update_gif()

    def update_gif(self):
        if hasattr(self, 'waddle_gif_label') and self.waddle_gif_label and self.waddle_images:
            new_waddle_image = self.waddle_images[self.current_waddle_frame]
            self.waddle_gif_label.configure(image=new_waddle_image)
            self.current_waddle_frame = (self.current_waddle_frame + 1) % len(self.waddle_images)
        
        if hasattr(self, 'kirby_gif_label') and self.kirby_gif_label and self.kirby_images:
            new_kirby_image = self.kirby_images[self.current_kirby_frame]
            self.kirby_gif_label.configure(image=new_kirby_image)
            self.current_kirby_frame = (self.current_kirby_frame + 1) % len(self.kirby_images)

        self.master.after(50, self.update_gif)


    def character_selection(self):
        self.character_selection_frame = Frame(self.master, bg="#f0f0f0")
        self.character_selection_frame.pack(fill=BOTH, expand=True)

        Button(self.character_selection_frame, text="Kirby !", command=self.welcome_screen, bg="#CE6A6C", height=3, width=10, fg="white").grid(row=3, column=5, pady=10, padx=20)
        Button(self.character_selection_frame, text="Waddle Dee !", command=self.welcome_screen, bg="#CE6A6C", height=3, width=10, fg="white").grid(row=3, column=1, pady=10, padx=20)

        # Waddle Dee GIF
        self.waddle_gif_label = Label(self.character_selection_frame)
        self.waddle_gif_label.grid(row=0, column=1, rowspan=3, padx=20, pady=20)

        # Kirby GIF
        self.kirby_gif_label = Label(self.character_selection_frame)
        self.kirby_gif_label.grid(row=0, column=5, rowspan=3, padx=20, pady=20)

        # Start the GIF animations
        self.animate_gif()


    def welcome_screen(self):
        self.character_selection_frame.pack_forget()
        
        # Clear the GIF label if it exists
        if hasattr(self, 'gif_label'):
            self.gif_label.pack_forget()
            self.gif_label = None
        
        self.welcome_screen_frame = Frame(self.master, bg="#F9C7BE")
        self.welcome_screen_frame.pack(fill=BOTH, expand=True)

        # Welcome labels
        welcome_label = Label(self.welcome_screen_frame, text="Welcome to [Game Name] !!", font=(self.kfont, 24), bg="#F9C7BE")
        welcome_label.pack(pady=20)  

        name_label = Label(self.welcome_screen_frame, text="Please enter your full name below:", font=(self.kfont, 15), bg="#F9C7BE")
        name_label.pack(pady=10)

        # Name's input box
        self.name_entry = Entry(self.welcome_screen_frame, font=(self.kfont, 12))
        self.name_entry.pack(pady=3, side=TOP)

        # Save name
        save_button = Button(self.welcome_screen_frame, text="Save", command=self.save_name, bg="#CE6A6C", height=2, width=20, fg="white")
        save_button.pack(pady=10)

        # Exit
        exit_button = Button(self.welcome_screen_frame, text="Exit", command=self.close_window, bg="#EDADA3", height=2, width=10, fg="white")
        exit_button.pack(side=BOTTOM, anchor=SE, padx=10, pady=10)

    def error_window(self, message):
        # Display an error message
        messagebox.showerror("Error", message)

    def save_name(self):
        # Get and validate the name entered by the user
        name = self.name_entry.get().strip()
        if re.match(r'^[a-zA-Z\s]+$', name):  # Check if name contains only letters and spaces
            self.player_name = name
            self.show_levels_screen()
        else:
            # Show an error message if the name is invalid
            messagebox.showerror("Error", "Please enter your name using letters a-z!")
            return  # Prevents proceeding with an invalid name
            
    def show_levels_screen(self):
        # Hide the welcome screen and show the levels screen
        self.welcome_screen_frame.pack_forget()
        self.levels_screen()

    def levels_screen(self):
        # Create the levels selection screen
        self.levels_frame = Frame(self.master, bg="#F9C7BE")
        self.levels_frame.pack(fill=BOTH, expand=True)

        # Add a label prompting the user to select a difficulty level
        label = Label(self.levels_frame, text="Please select your difficulty level:", font=(self.kfont, 16), bg="#F9C7BE")
        label.pack(pady=20)

        # Add buttons for each difficulty level
        button_easy = Button(self.levels_frame, text="Easy", command=self.run_easy, bg="#CE6A6C", height=6, width=20, fg="white")
        button_easy.pack(pady=10)

        button_medium = Button(self.levels_frame, text="Medium", command=self.run_medium, bg="#CE6A6C", height=6, width=20, fg="white")
        button_medium.pack(pady=10)

        button_hard = Button(self.levels_frame, text="Hard", command=self.run_hard, bg="#CE6A6C", height=6, width=20, fg="white")
        button_hard.pack(pady=10)

        # Add an exit button at the bottom right corner
        exit_button = Button(self.levels_frame, text="Exit", command=self.close_window, bg="#EDADA3", height=2, width=10, fg="white")
        exit_button.pack(side=BOTTOM, anchor=SE, padx=10, pady=10)

    def run_easy(self):
        # Hide the levels screen and start the easy level
        self.levels_frame.pack_forget()
        self.run_level(self.easy_question, "easy")

    def run_medium(self):
        # Hide the levels screen and start the medium level
        self.levels_frame.pack_forget()
        self.run_level(self.medium_question, "medium")

    def run_hard(self):
        # Hide the levels screen and start the hard level
        self.levels_frame.pack_forget()
        self.run_level(self.hard_question, "hard")

    def run_level(self, question_method, level):
        # Create the level screen
        self.level_frame = Frame(self.master, bg="#F9C7BE")
        self.level_frame.pack(fill=BOTH, expand=True)

        # Add a label for the question
        self.question_label = Label(self.level_frame, text="", font=(self.kfont, 16), bg="#F9C7BE")
        self.question_label.pack(pady=20)

        # Add an entry box for the user to enter their answer
        self.answer_entry = Entry(self.level_frame, font=(self.kfont, 12))
        self.answer_entry.pack(pady=10)

        # Add a label for feedback (correct/incorrect)
        self.feedback_label = Label(self.level_frame, text="", font=(self.kfont, 16), bg="#F9C7BE")
        self.feedback_label.pack(pady=10)

        # Add a button to submit the answer and go to the next question
        next_button = Button(self.level_frame, text="Next", command=self.check_answer, bg="#CE6A6C", height=2, width=10, fg="white")
        next_button.pack(pady=20)

        # Add an exit button at the bottom right corner of every level
        exit_button = Button(self.level_frame, text="Exit", command=self.close_window, bg="#EDADA3", height=2, width=10, fg="white")
        exit_button.pack(side=BOTTOM, anchor=SE, padx=10, pady=10)

        # Set the question method and level
        self.question_method = question_method
        self.level = level
        self.current_question = 0  # Reset question counter for the level
        self.correct_answers = 0  # Reset correct answers for the level
        self.score = 0  # Reset score for the level

        # Set total questions to 7
        self.total_questions = 7

        # Generate the first question
        self.question_method()

    def easy_question(self):
        # Generate a new easy question
        self.current_question += 1
        n1 = random.randint(10, 50)  # Generate the first random number
        n2 = random.randint(1, 10)  # Generate the second random number

        # Randomly choose between addition and subtraction
        operation = random.choice(["+", "-"])

        # Calculate the correct answer based on the chosen operation
        if operation == "+":
            self.correct_answer = n1 + n2
            question_text = f"What is {n1} + {n2}?"
        else:
            self.correct_answer = n1 - n2
            question_text = f"What is {n1} - {n2}?"

        # Display the question
        self.question_label.config(text=question_text)
        

    def medium_question(self):
        # Generate a new medium question
        self.current_question += 1
        operation = random.choice(["*", "/"])  # Multiplication and division

        n1 = random.randint(1, 10)  
        n2 = random.randint(11, 50)
        
        # No division by zero
        while operation == "/" and n2 == 0:
            n2 = random.randint(1, 12)
        
        # Calculate the correct answers
        if operation == "*":
            self.correct_answer = n1 * n2
            question_text = f"What is {n1} x {n2}?"
        else:
            self.correct_answer = n1 / n2
            question_text = f"What is {n1} ÷ {n2} (round to nearest whole number)?"
            self.correct_answer = round(self.correct_answer)  # Round to the nearest whole number

        # Display the question
        self.question_label.config(text=question_text)

    def hard_question(self):
        # Increment the current question count
        self.current_question += 1

        # Randomly select an operation from addition, subtraction, multiplication, and division
        operation = random.choice(["+", "-", "*", "/"])

        if operation == "*":
            n1 = random.randint(1, 10)  # Numbers up to 10 for multiplication
            n2 = random.randint(11, 30)  # Numbers between 11 and 30 for multiplication
            self.correct_answer = n1 * n2
            question_text = f"What is {n1} x {n2}?"
            
        elif operation == "/":
            n1 = random.randint(11, 30)  # Numerator between 11 and 30
            n2 = random.randint(2, 10)   # Denominator between 2 and 10, avoiding 0 and 1
            self.correct_answer = round(n1 / n2)  # Round to the nearest whole number
            question_text = f"What is {n1} ÷ {n2}?"

        elif operation == "+":
            n1 = random.randint(100, 999)  # Three-digit number for addition
            n2 = random.randint(100, 999)  # Three-digit number for addition
            self.correct_answer = n1 + n2
            question_text = f"What is {n1} + {n2}?"

        else:
            n1 = random.randint(100, 999)  # Three-digit number for subtraction
            n2 = random.randint(100, 999)  # Three-digit number for subtraction
            self.correct_answer = n1 - n2
            question_text = f"What is {n1} - {n2}?"

        # Display the question
        self.question_label.config(text=question_text)


        # Display the question
        self.question_label.config(text=question_text)

    def check_answer(self):
        user_answer = self.answer_entry.get().strip()

        if not user_answer:
            messagebox.showerror("Input Error", "Please enter an answer!")
            return

        if not re.match(r'^-?\d+$', user_answer):
            messagebox.showerror("Input Error", "Please enter a valid number!")
            return

        user_answer_int = int(user_answer)

        if user_answer_int == self.correct_answer:
            self.correct_answers += 1
            self.score += 10
            self.feedback_label.config(text="✓ Correct!", fg="green")

        else:
            self.score -= 6
            self.feedback_label.config(text=f"✗ Incorrect! The correct answer was {self.correct_answer}.", fg="red")

        self.master.after(1000, self.next_question)


    def next_question(self):
        if self.current_question < self.total_questions:
            self.answer_entry.delete(0, END)
            self.feedback_label.config(text="")

            self.question_method()
        else:
            self.show_results()


    def show_results(self):
        # Display the user's results in a message box
        result_message = f"You got {self.correct_answers} out of {self.total_questions} correct! Your final score is {self.score}."
        messagebox.showinfo("Results", result_message)

        # Save the player's name and score together
        if self.player_name:
            with open("saved_progress.txt", "a") as file:
                file.write(f"{self.player_name}: {self.score}\n")

        self.level_frame.pack_forget()  # Hide the level screen
        self.welcome_screen()  # Return to the home screen

    def close_window(self):
        self.master.destroy()

# Run 
root = Tk()
game = MathGame(root)
root.mainloop()