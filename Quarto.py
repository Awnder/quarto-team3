import tkinter as tk
from tkinter import ttk
from QuartoBot import QuartoTestBot
from GameBoard import GameBoard
from MenuScreen import MenuScreen
from VictoryChecker import VictoryChecker

class Quarto:
    def __init__(self):
        # initalize menu and game tk screens
        self.root = tk.Tk()
        self.canvas = None
        self.game_board = None

        # players
        self.player1_name = None
        self.player2_name = None
        self.turn = None # string state variable to track whose turn it is
        self.player_display = None # label that displays the current player
        self.bot = None # bot object if player 2 is a bot

        self.selected_piece = None  # Stores the currently selected piece's tag

        self.init_menu_screen()  # start game here at menu

        self.root.mainloop()

    def init_menu_screen(self):
        menu_screen = MenuScreen(self.root, self._start_game_callback)
        menu_screen.display()

    def _start_game_callback(self, player1_name: tk.StringVar, player2_name: tk.StringVar):
        """Callback function to start the game with the entered player names.
        Args:
            player1_name (tk.StringVar): The name of player 1
            player2_name (tk.StringVar): The name of player 2
        """
        self.init_game_screen(player1_name, player2_name)

    def init_game_screen(self, player1_name: tk.StringVar, player2_name: tk.StringVar):
        """
        creates a game screen so players can play quarto
        the goal is upon game end, tkinter will juggle between the menu and gameboard screen
        """
        # Clear current window
        if self.root:
            for widget in self.root.winfo_children():
                widget.destroy()

        # reuse existing root window and dynamically center it
        self.root.title("Quarto Game")
        self.root.geometry("1400x1000")
        self.canvas = tk.Canvas(self.root)
        self.canvas.pack(fill=tk.BOTH, expand=1)
        self.canvas.configure(bg="white")
        self.game_board = GameBoard(self.canvas)
        self.game_board.draw_board()  # draw the game board
        victory_checker = VictoryChecker(self.game_board.board, self.canvas)

        # if player name is empty just default to Player 1 or Player 2
        self.player1_name = "Player 1" if player1_name.get().strip() == "" else player1_name.get()
        self.player2_name = "Player 2" if player2_name.get().strip() == "" else player2_name.get()

        if self.player2_name == "QuartoTestBot":
            self.bot = QuartoTestBot()
        else:
            self.bot = None

        self.turn = self.player1_name

        self.player_display = tk.Label(self.root, text=f"{self.turn}'s Turn", font=("Courier", 15, "bold"), fg="seagreen")
        close_button = tk.Button(self.root, text="Close", command=self.init_menu_screen)
        self.player_display.pack(side=tk.TOP)
        close_button.pack(side=tk.BOTTOM)

        # victory handling
        claim_button = tk.Button(
            self.root, 
            text="Claim Victory",
            command=lambda: victory_checker.claim_victory(
                claim_direction_dropdown, 
                claim_location_dropdown, 
                claim_characteristic_dropdown
            )
        )

        claim_direction_label = tk.Label(self.root, text="Claim Direction: ")
        claim_direction_dropdown = ttk.Combobox(self.root, values=["row", "column", "diagonal"], state="readonly")
        claim_direction_dropdown.current(0)

        claim_location_label = tk.Label(self.root, text="Claim Number: ")
        claim_location_dropdown = ttk.Combobox(self.root, values=[1, 2, 3, 4], state="readonly")
        claim_location_dropdown.current(0)

        claim_characteristic_label = tk.Label(self.root, text="Claim Characteristic: ")
        claim_characteristic_dropdown = ttk.Combobox(self.root, values=["size", "color", "fill", "shape"], state="readonly")
        claim_characteristic_dropdown.current(0)

        claim_direction_dropdown.bind(
            "<<ComboboxSelected>>", 
            lambda event: self._update_combobox_location(
                claim_direction_dropdown, 
                claim_location_dropdown
            )
        )

        claim_button.pack(side=tk.RIGHT, padx=5)
        claim_location_dropdown.pack(side=tk.RIGHT, padx=5)
        claim_location_label.pack(side=tk.RIGHT, padx=5)
        claim_direction_dropdown.pack(side=tk.RIGHT, padx=5)
        claim_direction_label.pack(side=tk.RIGHT, padx=5)
        claim_characteristic_dropdown.pack(side=tk.RIGHT, padx=5)
        claim_characteristic_label.pack(side=tk.RIGHT, padx=5)

    ### TKINTER DYNAMIC UPDATE FUNCTIONS ###
    def _handle_bot_turn(self):
        """Handles the bot's turn if player 2 is a bot. It selects a piece and places it on the board."""
        if self.bot:
            # Select a piece for the human player
            self.selected_piece = self.bot.select_piece(self.game_board.board, self.piece_played)
        
            # Find a spot for the bot's move
            for i in range(4):
                for j in range(4):
                    if self.game_board.board[j][i] is None:  # Check if the slot is empty
                        tag = f"board-{i}-{j}"
                        self.place_piece(None, tag)  # Simulate click on an empty board spot
                        return  # Stop after placing one piece
            
            self._check_win_any()  # Check if the bot has won
        
    def _change_turn(self):
        """Changes turn and updates the display correctly"""
        self.turn = self.player1_name if self.turn == self.player2_name else self.player2_name  # Toggle turn

        if self.turn == self.player1_name:
            self.player_display.config(text=f"{self.player1_name}'s Turn", fg="seagreen")
        else:
            self.player_display.config(text=f"{self.player2_name}'s Turn", fg="purple4")
            self.root.after(500, self._handle_bot_turn)  # Ensure delay before bot plays

    def _update_opponent(self, opponent_dropdown: ttk.Combobox, player2_bot_dropdown: ttk.Combobox, player2_name_entry: tk.Entry, player2_name_label: tk.Label):
        """updates the player 2 name label and entry based on the opponent dropdown"""
        if opponent_dropdown.get() == "Bot":
            player2_name_label.config(text="Bot Name")
            player2_name_entry.grid_remove()
            player2_bot_dropdown.grid(row=3, column=1, pady=10)
        else:
            player2_name_label.config(text="Player 2 Name")
            player2_bot_dropdown.grid_remove()
            player2_name_entry.grid(row=3, column=1, pady=10)

    def _update_combobox_location(self, claim_direction_dropdown, claim_location_dropdown):
        """updates the claim number combobox based on the claim type combobox"""
        if claim_direction_dropdown.get() == "row" or claim_direction_dropdown.get() == "column":
            claim_location_dropdown["values"] = [1, 2, 3, 4]
            claim_location_dropdown.current(0)
        elif claim_direction_dropdown.get() == "diagonal":
            claim_location_dropdown["values"] = ["main", "anti"]
            claim_location_dropdown.current(0)

q = Quarto()
