import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from QuartoBot import QuartoTestBot


class Quarto:
    def __init__(self):
        # initalize menu and game tk screens
        self.root = None
        self.canvas = None
        self.board = None

        # players
        self.player1_name = None
        self.player2_name = None
        self.turn = None # string state variable to track whose turn it is
        self.player_display = None # label that displays the current player
        self.bot = None # bot object if player 2 is a bot

        # pieces
        self.small_small = 15
        self.small_large = 50
        self.large_small = 25
        self.large_large = 100
        self.selected_piece = None  # Stores the currently selected piece's tag
        self.piece_played = {}

        self.init_menu_screen()  # start game here at menu

        self.root.mainloop()

    def init_menu_screen(self):
        """
        creates a start screen for the game so players can input their names.
        the goal is after this first creation tkinter will juggle between the menu and gameboard screen
        """
        if self.root:
            self.root.destroy()

        # recreate tk interface for game menu
        self.root = tk.Tk()
        self.root.title("Quarto Menu")
        self.root.geometry("600x400")
        self.root.configure(bg="white")

        title = tk.Label(self.root, text="Welcome to Quarto", font=("Courier", 25, "bold"), bg="white")
        instruction = tk.Label(self.root, text="Enter Player Names to Begin!", font=("Courier", 15, "normal"))
        
        # player and bot widgets for labels, entries, and dropdowns
        # storing names in StringVar so they can be used later after the entries are destroyed when starting a new screen
        player1_name = tk.StringVar()
        player2_name = tk.StringVar()

        player1_name_label = tk.Label(self.root, text="Player 1 Name", font=("Courier", 15, "bold"), fg="seagreen")
        player1_name_entry = tk.Entry(self.root, textvariable=player1_name, font=("Courier", 12, "normal"), fg="seagreen", bg="lightgray")
        
        player2_name_label = tk.Label(self.root, text="Player 2 Name", font=("Courier", 15, "bold"), fg="purple4")
        player2_name_entry = tk.Entry(self.root, textvariable=player2_name, font=("Courier", 12, "normal"), fg="purple4", bg="lightgray")
        opponent_label = tk.Label(self.root, text="Use: QuartoTestBot for a Bot Player", font=("Courier", 10, "normal"), fg="purple4")

        submit_button = tk.Button(self.root, text="Start Game", command=lambda: self.init_game_screen(player1_name, player2_name), bg="lightgrey")

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

    def init_game_screen(self, player1_name: tk.StringVar, player2_name: tk.StringVar):
        """
        creates a game screen so players can play quarto
        the goal is upon game end, tkinter will juggle between the menu and gameboard screen
        """
        if self.root:
            self.root.destroy()

        # recreate tk interface for the game board
        self.root = tk.Tk()
        self.root.title("Quarto Game")
        self.root.geometry("1400x1000")
        self.canvas = tk.Canvas(self.root)
        self.canvas.pack(fill=tk.BOTH, expand=1)
        self.canvas.configure(bg="white")

        # if player name is empty just default to Player 1 or Player 2
        if player1_name.get().strip() == "":
            self.player1_name = "Player 1"
        else:
            self.player1_name = player1_name.get()
        if player2_name.get().strip() == "":
            self.player2_name = "Player 2"
        else:
            self.player2_name = player2_name.get()
        print(self.player2_name)
        if self.player2_name == "QuartoTestBot":
            self.bot = QuartoTestBot()
        else:
            self.bot = None

        self.turn = self.player1_name

        self.board = [[None for _ in range(4)] for _ in range(4)]  # creates a list of lists with 4 rows and 4 columns to fill in with pieces

        self.player_display = tk.Label(self.root, text=f"{self.turn}'s Turn", font=("Courier", 15, "bold"), fg="seagreen")
        close_button = tk.Button(self.root, text="Close", command=self.init_menu_screen)
        self.player_display.pack(side=tk.TOP)
        close_button.pack(side=tk.BOTTOM)

        # victory handling
        claim_button = tk.Button(self.root, text="Claim Victory", command=lambda: self.claim_victory(claim_direction_dropdown, claim_location_dropdown, claim_characteristic_dropdown))

        claim_direction_label = tk.Label(self.root, text="Claim Direction: ")
        claim_direction_dropdown = ttk.Combobox(self.root, values=["row", "column", "diagonal"], state="readonly")
        claim_direction_dropdown.current(0)

        claim_location_label = tk.Label(self.root, text="Claim Number: ")
        claim_location_dropdown = ttk.Combobox(self.root, values=[1, 2, 3, 4], state="readonly")
        claim_location_dropdown.current(0)

        claim_characteristic_label = tk.Label(self.root, text="Claim Characteristic: ")
        claim_characteristic_dropdown = ttk.Combobox(self.root, values=["size", "color", "fill", "shape"], state="readonly")
        claim_characteristic_dropdown.current(0)

        claim_direction_dropdown.bind("<<ComboboxSelected>>", lambda event: self._update_combobox_location(claim_direction_dropdown, claim_location_dropdown))

        claim_button.pack(side=tk.RIGHT, padx=5)
        claim_location_dropdown.pack(side=tk.RIGHT, padx=5)
        claim_location_label.pack(side=tk.RIGHT, padx=5)
        claim_direction_dropdown.pack(side=tk.RIGHT, padx=5)
        claim_direction_label.pack(side=tk.RIGHT, padx=5)
        claim_characteristic_dropdown.pack(side=tk.RIGHT, padx=5)
        claim_characteristic_label.pack(side=tk.RIGHT, padx=5)

    def select_piece(self, event, tag):
        """Selects a piece if clicked."""
        if self.piece_played[tag]:
            print(f"Piece {tag} has already been played!")
        else:
            self.selected_piece = tag
            print(f"Piece selected: {self.selected_piece}")
            self._change_turn()

    def place_piece(self, event, tag):
        """Places a selected piece on an empty grid slot."""
        if not self.selected_piece:
            print("No piece selected!")
            return

        # Get the grid slot tag
        _, i, j = tag.split("-")
        i, j = int(i), int(j)

        # Check if the slot is empty
        if self.board[j][i] is None:
            # Get grid slot coordinates
            x1, y1, x2, y2 = self.canvas.coords(tag)
            slot_center_x = (x1 + x2) / 2
            slot_center_y = (y1 + y2) / 2

            # Get box of the selected piece
            piece_coords = self.canvas.bbox(self.selected_piece)
            if piece_coords:
                piece_center_x = (piece_coords[0] + piece_coords[2]) / 2
                piece_center_y = (piece_coords[1] + piece_coords[3]) / 2

                # Calculate offsets to center the piece in the grid slot
                offset_x = slot_center_x - piece_center_x
                offset_y = slot_center_y - piece_center_y

                # Move all shapes associated with the tag
                self.canvas.move(self.selected_piece, offset_x, offset_y)
                self.canvas.tag_raise(self.selected_piece)
                self.canvas.update()  # Refresh

                # Mark the board as occupied
                self.board[j][i] = self.selected_piece
                print(f"Placed piece {self.selected_piece} at ({i}, {j})")
                self.piece_played[self.selected_piece] = True

                # Deselect the piece
                self.selected_piece = None
            else:
                print("Error: Could not get selected piece coordinates!")
        else:
            print(f"Slot ({i}, {j}) is already occupied!")

    ### TKINTER DYNAMIC UPDATE FUNCTIONS ###
    def _handle_bot_turn(self):
        """Handles the bot's turn if player 2 is a bot. It selects a piece and places it on the board."""
        if self.bot:
            # Select a piece for the human player
            self.selected_piece = self.bot.select_piece(self.board, self.piece_played)
        
            # Find a spot for the bot's move
            for i in range(4):
                for j in range(4):
                    if self.board[j][i] is None:  # Check if the slot is empty
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
