import tkinter as tk

class MenuScreen:
    def __init__(self, root: tk.Tk, start_game_callback):
        """
        Initializes the MenuScreen class.
        Uses a callback function to start the game to keep the game logic separate from the menu logic.

        Args:
            root (tk.Tk): The root Tkinter window.
            start_game_callback (function): A callback function to activate the game screen and start the game
        """
        self.root = root
        self.start_game_callback = start_game_callback
    
    def display(self):
        """Displays a Quarto menu screen with player name entries.
        Starts the game with the entered player names via the callback function
        """
        if self.root:
            for widget in self.root.winfo_children():
                widget.destroy()
        
        # recreate tk interface for game menu
        self.root.title("Quarto Menu")
        self.root.geometry("600x400")
        self.root.configure(bg="white")

        title = tk.Label(self.root, text="Welcome to Quarto", font=("Courier", 25, "bold"), bg="white")
        instruction = tk.Label(self.root, text="Enter Player Names to Begin!", font=("Courier", 15, "normal"))
        
        # player and bot widgets for labels, entries, and dropdowns
        # storing names in StringVar so they can be used later
        player1_name = tk.StringVar()
        player2_name = tk.StringVar()

        player1_name_label = tk.Label(self.root, text="Player 1 Name", font=("Courier", 15, "bold"), fg="seagreen")
        player1_name_entry = tk.Entry(self.root, textvariable=player1_name, font=("Courier", 12, "normal"), fg="seagreen", bg="lightgray")
        
        player2_name_label = tk.Label(self.root, text="Player 2 Name", font=("Courier", 15, "bold"), fg="purple4")
        player2_name_entry = tk.Entry(self.root, textvariable=player2_name, font=("Courier", 12, "normal"), fg="purple4", bg="lightgray")
        opponent_label = tk.Label(self.root, text="Use: QuartoTestBot for a Bot Player", font=("Courier", 10, "normal"), fg="purple4")

        # calls start game function defined in Quarto
        # this deletes the menu screen and creates a new game screen
        submit_button = tk.Button(
            self.root, 
            text="Start Game", 
            command=lambda: self.start_game_callback(player1_name, player2_name), 
            bg="lightgrey"
        )

        # centers widgets horizontally for each column
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        title.grid(row=0, column=0, columnspan=2, pady=20)
        instruction.grid(row=1, column=0, columnspan=2, pady=10)
        player1_name_label.grid(row=2, column=0, pady=10)
        player2_name_label.grid(row=2, column=1, pady=10)
        player1_name_entry.grid(row=3, column=0, pady=10)
        player2_name_entry.grid(row=3, column=1, pady=10)
        opponent_label.grid(row=4, column=0, columnspan=2, pady=10)
        submit_button.grid(row=6, column=0, columnspan=2, pady=10)
