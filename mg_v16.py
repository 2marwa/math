from tkinter import *
import re
import random
from tkinter import messagebox
from PIL import Image, ImageTk  # pip install Pillow
import os

class MathGame:
    def __init__(self, master):
        """
        Initialize the MathGame application.
        
        """
        self.master = master
        master.title("Math Game")
        master.configure(borderwidth=10, relief='ridge', bg="#fefcbf") # Pale yellow border
        master.geometry("800x600")  # Set the window size

        self.kfont = ("Kristen ITC")  # Font used in the application
        self.current_question = 0  # Track the current question number
        self.correct_answers = 0  # Track the number of correct answers
        self.score = 0  # Initialize the score
        self.player_name = None  # Initialize the player's name
        self.level = 1  # Start with Level 1

        # Load GIF images
        self.gif_path = os.path.join(os.path.dirname(__file__), "waddle jump.gif")
        self.load_gif()

        # Start the character selection screen
        self.character_selection()

    def load_gif(self):
        """
        Load GIF images for character animations.
        """
        try:
            # Load Waddle Dee GIF
            self.waddle_gif_path = os.path.join(os.path.dirname(__file__), "waddle jump.gif")
            openImage = Image.open(self.waddle_gif_path)
            frames = openImage.n_frames
            self.waddle_images = [PhotoImage(file=self.waddle_gif_path, format=f"gif -index {i}") for i in range(frames)]

            # Load Kirby GIF
            self.kirby_gif_path = os.path.join(os.path.dirname(__file__), "kirby jump.gif")
            openImage = Image.open(self.kirby_gif_path)
            frames = openImage.n_frames
            self.kirby_images = [PhotoImage(file=self.kirby_gif_path, format=f"gif -index {i}") for i in range(frames)]
        except Exception as e:
            print(f"Error loading GIF: {e}")

    def animate_gif(self):
        """
        Start the GIF animation for both characters.
        """
        if hasattr(self, 'waddle_gif_label') and self.waddle_gif_label:
            self.current_waddle_frame = 0
        if hasattr(self, 'kirby_gif_label') and self.kirby_gif_label:
            self.current_kirby_frame = 0
        self.update_gif()

    def update_gif(self):
        """
        Update the GIF images at regularly.
        """
        if hasattr(self, 'waddle_gif_label') and self.waddle_gif_label and self.waddle_images:
            new_waddle_image = self.waddle_images[self.current_waddle_frame]
            self.waddle_gif_label.configure(image=new_waddle_image)
            self.current_waddle_frame = (self.current_waddle_frame + 1) % len(self.waddle_images)
        
        if hasattr(self, 'kirby_gif_label') and self.kirby_gif_label and self.kirby_images:
            new_kirby_image = self.kirby_images[self.current_kirby_frame]
            self.kirby_gif_label.configure(image=new_kirby_image)
            self.current_kirby_frame = (self.current_kirby_frame + 1) % len(self.kirby_images)

        self.master.after(100, self.update_gif)  # Update every 100 milliseconds

    def set_background_image(self, frame, image_path):
        try:
            image = Image.open(image_path)
            photo = ImageTk.PhotoImage(image)
            background_label = Label(frame, image=photo)
            background_label.image = photo  # To stop it from dissappearing from the widget
            background_label.place(relwidth=1, relheight=1)  # Cover the entire frame
        except Exception as e:
            print(f"Error loading background image: {e}")


    def character_selection(self):
        """
        Display the character selection screen.
        """
        self.character_selection_frame = Frame(self.master, bg="#f0f0f0")
        self.character_selection_frame.pack(fill=BOTH, expand=True)

        # Configure columns to evenly distribute space
        for i in range(12):  # 12 columns in total
            self.character_selection_frame.columnconfigure(i, weight=1)

        # Waddle Dee GIF
        self.waddle_gif_label = Label(self.character_selection_frame)
        self.waddle_gif_label.grid(row=0, column=2, rowspan=3, padx=20, pady=20, columnspan=3, sticky="n")

        # Kirby GIF
        self.kirby_gif_label = Label(self.character_selection_frame)
        self.kirby_gif_label.grid(row=0, column=5, rowspan=3, padx=20, pady=20, columnspan=3, sticky="n")

        # Buttons for character selection
        Button(self.character_selection_frame, text="Kirby!", command=self.welcome_screen, bg="#fefcbf", height=4, width=10, fg="black").grid(row=5, column=5, pady=10, padx=20, columnspan=3, sticky="n")
        Button(self.character_selection_frame, text="Waddle Dee!", command=self.welcome_screen, bg="#fefcbf", height=4, width=10, fg="black").grid(row=5, column=2, pady=10, padx=20, columnspan=3, sticky="n")

        # Start the GIF animations
        self.animate_gif()

        

    def welcome_screen(self):
        """
        Display the welcome screen where the user enters their name.
        """
        self.character_selection_frame.pack_forget()  # Hide the character selection screen

        # Clear the GIF label if it exists
        if hasattr(self, 'gif_label'):
            self.gif_label.pack_forget()
            self.gif_label = None
        
        self.welcome_screen_frame = Frame(self.master, bg="#F9C7BE")
        self.welcome_screen_frame.pack(fill=BOTH, expand=True)

        # Set the background image for the welcome screen
        self.set_background_image(self.welcome_screen_frame, os.path.join(os.path.dirname(__file__), "dreamland_1.jpg"))

        # Welcome labels
        welcome_label = Label(self.welcome_screen_frame, text="Star Sum\nQuest", font=(self.kfont, 24), bg= "#827bff")
        welcome_label.pack(pady=20)

        name_label = Label(self.welcome_screen_frame, text="Please enter your name below:", font=(self.kfont, 15), bg= "#96e6fd")
        name_label.pack(pady=10)

        # Name's input box
        self.name_entry = Entry(self.welcome_screen_frame, font=(self.kfont, 12))
        self.name_entry.pack(pady=3, side=TOP)

        # Save name button
        save_button = Button(self.welcome_screen_frame, text="Save", command=self.save_name, bg="#fefcbf", height=2, width=20, fg="black", font = ("Kristen ITC", 10))
        save_button.pack(pady=10)

        # Exit button
        exit_button = Button(self.welcome_screen_frame, text="Exit", command=self.close_window, bg="#fefcbf", height=2, width=10, fg="black", font = ("Kristen ITC", 10))
        exit_button.pack(side=BOTTOM, anchor=SE, padx=10, pady=10)

    def error_window(self, message):
        """
        Display an error message in a popup window.
        
        :param message: The error message to display.
        """
        messagebox.showerror("Error", message)

    def save_name(self):
        """
        Validate and save the player's name.
        """
        name = self.name_entry.get().strip()
        if re.match(r'^[a-zA-Z\s]+$', name):  # Validation
            self.player_name = name
            self.start_level()
        else:
            # Show an error message if the name is invalid
            messagebox.showerror("Error", "Please enter your name using letters a-z!")
            return  

    def start_level(self):
        """
        Hide the welcome screen and start Level 1.
        """
        self.welcome_screen_frame.pack_forget()
        self.run_level(self.level1_question, "Level 1")


    def run_level(self, question_method, level):
        """
        Set up and display the level screen.
        
        :param question_method: The method used to generate questions for the level.
        :param level: The difficulty level of the game.
        """
        self.level_frame = Frame(self.master, bg="#c0e3ed")
        self.level_frame.pack(fill=BOTH, expand=True)


        # Display the score in the top right corner
        self.score_label = Label(self.level_frame, text=f"Score: {self.score}", font=(self.kfont, 12), bg="#F9C7BE")
        self.score_label.pack(anchor=NE, padx=10, pady=5)

        # Display the question label
        self.question_label = Label(self.level_frame, text="", font=(self.kfont, 16), bg="#F9C7BE")
        self.question_label.pack(pady=20)

        # Answer entry box
        self.answer_entry = Entry(self.level_frame, font=(self.kfont, 12))
        self.answer_entry.pack(pady=10)

        # Feedback label
        self.feedback_label = Label(self.level_frame, text="", font=(self.kfont, 16), bg="#F9C7BE")
        self.feedback_label.pack(pady=10)

        # Next question button
        next_button = Button(self.level_frame, text="Next", command=self.check_answer, bg="#CE6A6C", height=2, width=10, fg="white")
        next_button.pack(pady=20)

        # Exit button
        exit_button = Button(self.level_frame, text="Exit", command=self.close_window, bg="#EDADA3", height=2, width=10, fg="white")
        exit_button.pack(side=BOTTOM, anchor=SE, padx=10, pady=10)

        # Set the question method and level
        self.question_method = question_method
        self.level = level
        self.current_question = 0  # Reset question counter for the level
        self.correct_answers = 0  # Reset correct answers for the level

        # Set total questions to 5 for levels 1-4, 10 for level 5
        self.total_questions = 5 if level != "Level 5" else 10

        # Generate the first question
        self.question_method()


    def level1_question(self):
        """
        Generate a new Level 1 question (simple addition).
        """
        self.current_question += 1
        n1 = random.randint(1, 10)
        n2 = random.randint(1, 10)
        self.correct_answer = n1 + n2
        question_text = f"What is {n1} + {n2}?"
        self.question_label.config(text=question_text)

    def level2_question(self):
        """
        Generate a new Level 2 question (simple subtraction).
        """
        self.current_question += 1
        n1 = random.randint(1, 25)
        n2 = random.randint(1, 25)
        self.correct_answer = n1 - n2
        question_text = f"What is {n1} - {n2}?"
        self.question_label.config(text=question_text)

    def level3_question(self):
        """
        Generate a new Level 3 question (basic multiplication).
        """
        self.current_question += 1
        n1 = random.randint(1, 12)
        n2 = random.randint(1, 12)
        self.correct_answer = n1 * n2
        question_text = f"What is {n1} x {n2}?"
        self.question_label.config(text=question_text)

    def level4_question(self):
        """
        Generate a new Level 4 question (basic division).
        """
        self.current_question += 1
        n1 = random.randint(1, 12) * random.randint(1, 12)  # Ensure n1 is a multiple of n2
        n2 = random.randint(1, 12)
        self.correct_answer = round(n1 / n2)
        question_text = f"What is {n1} ÷ {n2} (round to nearest whole number)?"
        self.question_label.config(text=question_text)

    def level5_question(self):
        """
        Generate a new Level 5 question (all operations plus squaring numbers).
        """
        self.current_question += 1
        operation = random.choice(["+", "-", "*", "/", "^"])

        if operation == "^":
            n = random.randint(1, 12)
            self.correct_answer = n ** 2
            question_text = f"What is {n} squared?"
        else:
            n1 = random.randint(1, 12)
            n2 = random.randint(1, 12)

            if operation == "+":
                self.correct_answer = n1 + n2
                question_text = f"What is {n1} + {n2}?"
            elif operation == "-":
                self.correct_answer = n1 - n2
                question_text = f"What is {n1} - {n2}?"
            elif operation == "*":
                self.correct_answer = n1 * n2
                question_text = f"What is {n1} x {n2}?"
            else:
                # Ensure n2 is not zero for division
                n2 = random.randint(1, 12)
                self.correct_answer = round(n1 / n2)
                question_text = f"What is {n1} ÷ {n2} (round to nearest whole number)?"

        self.question_label.config(text=question_text)

    def check_answer(self):
        """
        Check the user's answer and provide feedback.
        """
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
            
            # Adjust points based on level
            level_points = {"Level 1": 10, "Level 2": 20, "Level 3": 30, "Level 4": 40, "Level 5": 50}
            self.score += level_points.get(self.level, 0)
            
            self.feedback_label.config(text=" ✓ ", fg="green") # Correct answer message
            self.score_label.config(text=f"Score: {self.score}")  # Update the score label
        else:
            self.feedback_label.config(text=f" ✗ {self.correct_answer}", fg="red") # Incorrect answer message

        # Move to the next question after a short delay
        self.master.after(1000, self.next_question)

    def next_question(self):
        """
        Move to the next question or show results if all questions are answered.
        """
        if self.current_question < self.total_questions:
            self.answer_entry.delete(0, END)
            self.feedback_label.config(text="")
            self.question_method()
        else:
            self.show_level_complete()

    def show_level_complete(self):
        """
        Show a screen when the level is completed.
        """
        self.level_frame.pack_forget()  # Hide the level screen
        
        self.level_complete_frame = Frame(self.master, bg="#F9C7BE")
        self.level_complete_frame.pack(fill=BOTH, expand=True)

        # Display level completion message
        level_complete_label = Label(self.level_complete_frame, text=f"Congratulations! You've completed Level {self.level}!", font=(self.kfont, 24), bg="#F9C7BE")
        level_complete_label.pack(pady=20)

        # Next level button
        next_level_button = Button(self.level_complete_frame, text="Next Level", command=self.next_level, bg="#CE6A6C", height=2, width=20, fg="white")
        next_level_button.pack(pady=10)

        # Exit button
        exit_button = Button(self.level_complete_frame, text="Exit", command=self.close_window, bg="#EDADA3", height=2, width=10, fg="white")
        exit_button.pack(side=BOTTOM, anchor=SE, padx=10, pady=10)


    def next_level(self):
        """
        Advance to the next level.
        """
        if hasattr(self, 'level_complete_frame') and self.level_complete_frame.winfo_ismapped():
            self.level_complete_frame.pack_forget()  # Hide the current frame

        # Extract the numeric part of the level from the string and compare it
        try:
            current_level_number = int(self.level.split()[-1])
        except (IndexError, ValueError):
            # Handle the case where the level string is not in the expected format
            print("Error: Invalid level format")
            return

        if current_level_number < 5:  # If the current level is less than five, then advance to next level, otherwise end game and show results.
            self.level = f'Level {current_level_number + 1}'
            
            # Directly pass the appropriate question method based on the level
            if self.level == 'Level 1':
                self.run_level(self.level1_question, self.level)
            elif self.level == 'Level 2':
                self.run_level(self.level2_question, self.level)
            elif self.level == 'Level 3':
                self.run_level(self.level3_question, self.level)
            elif self.level == 'Level 4':
                self.run_level(self.level4_question, self.level)
            elif self.level == 'Level 5':
                self.run_level(self.level5_question, self.level)
            else:
                print("Error: Unexpected level")
        else:
            self.show_results()




    def show_results(self):
        """
        Display the user's results and save progress.
        """
        # Display the user's results in a message box
        result_message = f"Your final score is {self.score}."
        messagebox.showinfo("Results", result_message)

        # Save the player's name and score together
        if self.player_name:
            with open("saved_progress.txt", "a") as file:
                file.write(f"{self.player_name}: {self.score}\n")

        self.level_complete_frame.pack_forget()  # Hide the level complete screen

        if hasattr(self, 'level_complete_frame'):
            self.level_complete_frame.pack_forget()
        if hasattr(self, 'welcome_screen_frame'):
            self.welcome_screen_frame.pack_forget()

        self.character_selection()  # Return to the character selection screen



    def close_window(self):
        """
        Close the application window.
        """
        self.master.destroy()

# Run the application
root = Tk()
game = MathGame(root)
root.mainloop()
