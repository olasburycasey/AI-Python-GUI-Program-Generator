import tkinter as tk
import random

# Dictionary of countries and their capitals (replace with a full list for a complete game)
country_capitals = {
    "USA": "Washington D.C.",
    "Canada": "Ottawa",
    "UK": "London",
    "France": "Paris",
    "Germany": "Berlin",
    "Japan": "Tokyo",
    "Australia": "Canberra",
    "Brazil": "Brasilia",
    "India": "New Delhi",
    "China": "Beijing",
    "Egypt": "Cairo",
    "South Africa": "Pretoria",  # or Cape Town or Bloemfontein, complex
    "Russia": "Moscow",
    "Mexico": "Mexico City",
    "Italy": "Rome",
    "Spain": "Madrid",
    "Argentina": "Buenos Aires",
    "Nigeria": "Abuja",
    "Sweden": "Stockholm",
    "Netherlands": "Amsterdam",
    "Switzerland": "Bern",
    "Belgium": "Brussels",
    "Austria": "Vienna",
    "Portugal": "Lisbon",
    "Greece": "Athens",
    "Ireland": "Dublin",
    "Denmark": "Copenhagen",
    "Norway": "Oslo",
    "Finland": "Helsinki",
    "Poland": "Warsaw",
    "Czech Republic": "Prague",
    "Hungary": "Budapest",
    "Romania": "Bucharest",
    "Ukraine": "Kyiv",
    "Turkey": "Ankara",
    "Israel": "Jerusalem",
    "Saudi Arabia": "Riyadh",
    "Indonesia": "Jakarta",
    "Thailand": "Bangkok",
    "Vietnam": "Hanoi",
    "Philippines": "Manila",
    "Malaysia": "Kuala Lumpur",
    "Singapore": "Singapore",
    "New Zealand": "Wellington",
    "Chile": "Santiago",
    "Colombia": "Bogota",
    "Peru": "Lima",
    "Venezuela": "Caracas",
    "Kenya": "Nairobi",
    "Morocco": "Rabat",
    "Algeria": "Algiers",
    "Ghana": "Accra",
    "Ivory Coast": "Yamoussoukro",  # Administrative Capital
    "Angola": "Luanda",
    "Cameroon": "Yaounde",
    "Zimbabwe": "Harare",
    "Zambia": "Lusaka",
    "Uganda": "Kampala",
    "Ethiopia": "Addis Ababa",
    "Iran": "Tehran",
    "Iraq": "Baghdad",
    "Afghanistan": "Kabul",
    "Pakistan": "Islamabad",
    "Bangladesh": "Dhaka",
    "Nepal": "Kathmandu",
    "Myanmar": "Naypyidaw",
    "North Korea": "Pyongyang",
    "South Korea": "Seoul",
    "Taiwan": "Taipei"

}  # Add more countries to this dictionary


class CapitalGuessingGame:
    def __init__(self, master):
        self.master = master
        master.title("Guess the Capital!")

        self.countries = sorted(list(country_capitals.keys()))  # Sort countries alphabetically
        self.current_country = ""
        self.score = 0
        self.total_questions = 0

        # UI elements
        self.country_label = tk.Label(master, text="", font=("Arial", 20))
        self.country_label.pack(pady=20)

        self.entry_var = tk.StringVar()
        self.capital_entry = tk.Entry(master, textvariable=self.entry_var, font=("Arial", 16))
        self.capital_entry.pack(pady=10)

        self.submit_button = tk.Button(master, text="Submit", command=self.check_answer, font=("Arial", 14))
        self.submit_button.pack(pady=10)

        self.result_label = tk.Label(master, text="", font=("Arial", 14))
        self.result_label.pack(pady=10)

        self.score_label = tk.Label(master, text="Score: 0 / 0", font=("Arial", 12))
        self.score_label.pack(pady=5)

        self.new_game_button = tk.Button(master, text="New Game", command=self.start_game, font=("Arial", 12))
        self.new_game_button.pack(pady=10)

        self.message_label = tk.Label(master, text="", font=("Arial", 10))  # For helpful messages
        self.message_label.pack(pady=5)


        self.start_game()

    def start_game(self):
        self.countries = sorted(list(country_capitals.keys()))  # Reset and sort for new game
        self.score = 0
        self.total_questions = 0
        self.score_label.config(text="Score: 0 / 0")
        self.get_new_country()
        self.capital_entry.config(state=tk.NORMAL)  # Enable the entry
        self.entry_var.set("")  # Clear the entry field
        self.result_label.config(text="")
        self.message_label.config(text="" )
        self.submit_button.config(state=tk.NORMAL) # Enable Submit button


    def get_new_country(self):
        if not self.countries:
             self.country_label.config(text="Game Over! No more countries.")
             self.capital_entry.config(state=tk.DISABLED) # Disable the input
             self.submit_button.config(state=tk.DISABLED) # Disable the submit button
             return


        self.current_country = random.choice(self.countries)
        self.country_label.config(text=f"What is the capital of {self.current_country}?")

    def check_answer(self):
        capital = self.entry_var.get().strip()  # Remove leading/trailing spaces
        correct_capital = country_capitals[self.current_country]

        if capital.lower() == correct_capital.lower():
            self.result_label.config(text="Correct!", fg="green")
            self.score += 1
        else:
            self.result_label.config(text=f"Incorrect. The capital is {correct_capital}.", fg="red")

        self.total_questions += 1
        self.score_label.config(text=f"Score: {self.score} / {self.total_questions}")

        # Remove the country from the list after it's been used
        self.countries.remove(self.current_country)  # Very Important!
        self.entry_var.set("")  # Clear the entry for the next question
        self.master.after(1500, self.get_new_country) # Slight delay before next question

        if not self.countries:
             self.country_label.config(text="Game Over!  You answered all the countries.")
             self.capital_entry.config(state=tk.DISABLED) # Disable the input
             self.submit_button.config(state=tk.DISABLED) # Disable the submit button
             self.message_label.config(text=f"Final Score: {self.score} / {self.total_questions}", font=("Arial", 14, "bold")) # Show the final score



root = tk.Tk()
game = CapitalGuessingGame(root)
root.mainloop()
