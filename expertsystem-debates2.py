import tkinter as tk
from tkinter import font

class DebaterGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Debater Guessing Game")
        self.root.state('zoomed')  # Make the window fullscreen
        
        # Font Configuration
        self.bold_font = font.Font(family="Helvetica", size=18, weight="bold")

        # Introduction
        self.intro_frame = tk.Frame(self.root)
        self.intro_frame.pack(expand=True)
        
        intro_label = tk.Label(self.intro_frame, text="Welcome to the Debater Guessing Game!", font=self.bold_font)
        intro_label.pack(pady=20)
        
        intro_desc = tk.Label(self.intro_frame, text="Think of a debater, and I'll try to guess who it is!", font=("Helvetica", 14))
        intro_desc.pack(pady=10)
        
        debater_list_label = tk.Label(self.intro_frame, text="Debaters: Muzzammil, Ammar, Laraib, Midhah, Zainab, Atiya, Fatima, Rameen, Ibba, Ezzah, Shahmir", font=("Helvetica", 12))
        debater_list_label.pack(pady=20)

        start_button = tk.Button(self.intro_frame, text="Start Game", font=self.bold_font, command=self.start_game)
        start_button.pack(pady=20)
        
        # Game frame for questions
        self.game_frame = tk.Frame(self.root)

        # Debaters and attributes
        self.create_debaters()
        self.current_question = 0
        self.selected_debater = None

    def create_debaters(self):
        self.debaters = [
            {"name": "Muzzammil", "first_speaker": False, "still_in_camp": True, "often_in_class": True, "junior_nationals": True, "hit_by_marker": True, "second_speaker": True, "third_speaker": True, "quarter_finals": True, "won_tournament": False, "above_72": True, "middle_schooler": False, "joined_after_2023": False},
            {"name": "Ammar", "first_speaker": False, "still_in_camp": True, "often_in_class": True, "junior_nationals": True, "hit_by_marker": True, "second_speaker": True, "third_speaker": True, "quarter_finals": True, "won_tournament": False, "above_72": False, "middle_schooler": False, "joined_after_2023": True},
            {"name": "Laraib", "first_speaker": True, "still_in_camp": True, "often_in_class": True, "junior_nationals": False, "hit_by_marker": False, "second_speaker": False, "third_speaker": False, "quarter_finals": True, "won_tournament": False, "above_72": True, "middle_schooler": False, "joined_after_2023": False},
            {"name": "Midhah", "first_speaker": True, "still_in_camp": True, "often_in_class": True, "junior_nationals": True, "hit_by_marker": False, "second_speaker": True, "third_speaker": False, "quarter_finals": True, "won_tournament": False, "above_72": True, "middle_schooler": False, "joined_after_2023": False},
            {"name": "Zainab", "first_speaker": True, "still_in_camp": True, "often_in_class": True, "junior_nationals": False, "hit_by_marker": False, "second_speaker": False, "third_speaker": False, "quarter_finals": True, "won_tournament": False, "above_72": False, "middle_schooler": False, "joined_after_2023": True},
            {"name": "Atiya", "first_speaker": True, "still_in_camp": False, "often_in_class": False, "junior_nationals": True, "hit_by_marker": False, "second_speaker": False, "third_speaker": False, "quarter_finals": True, "won_tournament": True, "above_72": False, "middle_schooler": False, "joined_after_2023": False},
            {"name": "Fatima", "first_speaker": False, "still_in_camp": False, "often_in_class": False, "junior_nationals": True, "hit_by_marker": False, "second_speaker": False, "third_speaker": True, "quarter_finals": False, "won_tournament": False, "above_72": True, "middle_schooler": False, "joined_after_2023": False},
            {"name": "Rameen", "first_speaker": False, "still_in_camp": True, "often_in_class": False, "junior_nationals": True, "hit_by_marker": False, "second_speaker": True, "third_speaker": True, "quarter_finals": True, "won_tournament": False, "above_72": False, "middle_schooler": False, "joined_after_2023": False},
            {"name": "Ibba", "first_speaker": False, "still_in_camp": True, "often_in_class": False, "junior_nationals": False, "hit_by_marker": False, "second_speaker": True, "third_speaker": True, "quarter_finals": True, "won_tournament": False, "above_72": False, "middle_schooler": False, "joined_after_2023": True},
            {"name": "Ezzah", "first_speaker": False, "still_in_camp": True, "often_in_class": True, "junior_nationals": False, "hit_by_marker": False, "second_speaker": True, "third_speaker": False, "quarter_finals": False, "won_tournament": False, "above_72": False, "middle_schooler": True, "joined_after_2023": True},
            {"name": "Shahmir", "first_speaker": False, "still_in_camp": True, "often_in_class": True, "junior_nationals": False, "hit_by_marker": True, "second_speaker": False, "third_speaker": False, "quarter_finals": True, "won_tournament": False, "above_72": False, "middle_schooler": False, "joined_after_2023": True}
        ]
        self.create_questions()

    def create_questions(self):
        self.questions = [
            ("Did this debater go as a 1st speaker in a tournament?", "first_speaker"),
            ("Is this debater still part of the camp?", "still_in_camp"),
            ("Does this debater come to the class often?", "often_in_class"),
            ("Did this debater go to the junior nationals 24’?", "junior_nationals"),
            ("Did your debater ever get hit by a marker?", "hit_by_marker"),
            ("Did this debater go as the 2nd speaker in a tournament?", "second_speaker"),
            ("Did this debater go as the 3rd speaker in a tournament?", "third_speaker"),
            ("Did your debater ever go to the quarter finals?", "quarter_finals"),
            ("Did your debater ever win a tournament?", "won_tournament"),
            ("Did your debater ever get above or equal to 72?", "above_72"),
            ("Is your debater a middle schooler?", "middle_schooler"),
            ("Did your debater join in or after 2023?", "joined_after_2023")
        ]

    def start_game(self):
        # Transition to the game frame
        self.intro_frame.pack_forget()
        self.game_frame.pack(expand=True)
        self.display_question()

    def display_question(self):
        # Remove previous widgets
        for widget in self.game_frame.winfo_children():
            widget.destroy()

        # Check if we've asked all questions
        if self.current_question < len(self.questions):
            question_text, attribute = self.questions[self.current_question]

            # Display the question
            question_label = tk.Label(self.game_frame, text=question_text, font=self.bold_font)
            question_label.pack(pady=50)

            # Yes/No buttons
            button_frame = tk.Frame(self.game_frame)
            button_frame.pack(pady=20)

            yes_button = tk.Button(button_frame, text="Yes", font=self.bold_font, command=lambda: self.answer_question(True))
            yes_button.pack(side=tk.LEFT, padx=20)

            no_button = tk.Button(button_frame, text="No", font=self.bold_font, command=lambda: self.answer_question(False))
            no_button.pack(side=tk.LEFT, padx=20)

        else:
            self.identify_debater()

    def answer_question(self, answer):
        question_text, attribute = self.questions[self.current_question]

        # Filter debaters based on the answer
        self.debaters = [debater for debater in self.debaters if debater[attribute] == answer]

        # Move to the next question
        self.current_question += 1
        self.display_question()

    def identify_debater(self):
        # Display the identified debater
        if len(self.debaters) == 1:
            result_text = f"The debater is {self.debaters[0]['name']}!"
        else:
            result_text = "I couldn't identify the debater. Please restart the game."

        result_label = tk.Label(self.game_frame, text=result_text, font=self.bold_font)
        result_label.pack(pady=50)

        # Optionally you can restart the game by showing a message to close and restart manually
        restart_info = tk.Label(self.game_frame, text="Close and restart the game manually to try again.", font=("Helvetica", 14))
        restart_info.pack(pady=20)

# Create the main application window
root = tk.Tk()
game = DebaterGuessingGame(root)
root.mainloop()
