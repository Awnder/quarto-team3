import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class Quarto:
    def __init__(self):
        # initalize menu and game tk screens
        self.root = None
        self.canvas = None
        self.board = None

        # players
        self.player1_name = None
        self.player2_name = None
        self.state = "Player 2 Selects"
        self.possible_states = ["Player 2 Selects", "Player 1 Places", "Player 1 Selects", "Player 2 Places"]
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
        Creates a start screen for the game so players can input their names.
        """

        if self.root:
            self.root.destroy()

        self.root = tk.Tk()
        self.root.title("Quarto Menu")
        self.root.geometry("600x400")
        self.root.configure(bg="white")

        title_font = ("Helvetica", 24, "bold")
        label_font = ("Helvetica", 14, "bold")
        entry_font = ("Helvetica", 12)
        note_font = ("Helvetica", 10, "italic")

        title = tk.Label(self.root, text="Welcome to Quarto", font=title_font, bg="white", fg="#222222")
        instruction = tk.Label(self.root, text="Enter Player Names to Begin!", font=("Helvetica", 16), bg="white", fg="#333333")

        # StringVars
        player1_name = tk.StringVar()
        player2_name = tk.StringVar()

        # Player 1 Widgets
        player1_name_label = tk.Label(self.root, text="Player 1 Name", font=label_font, fg="#2E8B57", bg="white")
        player1_name_entry = tk.Entry(self.root, textvariable=player1_name, font=entry_font, fg="black", bg="#f0f0f0")

        # Player 2 Widgets
        player2_name_label = tk.Label(self.root, text="Player 2 Name", font=label_font, fg="#6A0DAD", bg="white")
        player2_name_entry = tk.Entry(self.root, textvariable=player2_name, font=entry_font, fg="black", bg="#f0f0f0")

        # Notes
        opponent_label1 = tk.Label(self.root, text="Use: QuartoTestBot for a Bot Player", font=note_font, fg="#6A0DAD", bg="white")
        opponent_label2 = tk.Label(self.root, text="Use: SmarterQuartoBot for a Smart Bot Player", font=note_font, fg="#6A0DAD", bg="white")

        # Button
        submit_button = tk.Button(self.root, text="Start Game", font=entry_font,
                              command=lambda: self.init_game_screen(player1_name, player2_name),
                              bg="#ffffff", fg="#000000", highlightbackground="#333333")

        # Layout
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        title.grid(row=0, column=0, columnspan=2, pady=(20, 10))
        instruction.grid(row=1, column=0, columnspan=2, pady=(0, 15))

        player1_name_label.grid(row=2, column=0, pady=5)
        player2_name_label.grid(row=2, column=1, pady=5)

        player1_name_entry.grid(row=3, column=0, pady=5, ipadx=20)
        player2_name_entry.grid(row=3, column=1, pady=5, ipadx=20)

        opponent_label1.grid(row=4, column=0, columnspan=2, pady=(10, 2))
        opponent_label2.grid(row=5, column=0, columnspan=2, pady=(0, 20))

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
            from QuartoBot import QuartoTestBot
            self.bot = QuartoTestBot()
            # change_turn is called on piece place and select
            # however, since the bot turn will never fire until a click happens,
            # we need to call it here to ensure the bot plays
            self.root.after(500, self.handle_bot_select)
        elif self.player2_name == "SmarterQuartoBot":
            from QuartoBot import SmarterQuartoBot  # make sure the bot is defined there
            self.bot = SmarterQuartoBot()
            self.root.after(500, self.handle_bot_select)
        else:
            self.bot = None

        self.draw_board()
        self._bind_highlight()
        self._bind_clicks()
        self.board = [[None for _ in range(4)] for _ in range(4)]  # creates a list of lists with 4 rows and 4 columns to fill in with pieces

        self.player_display = tk.Label(self.root, text=f"{self.state}", font=("Courier", 15, "bold"), fg="seagreen")
        close_button = tk.Button(self.root, text="Close", command=self.init_menu_screen)
        self.player_display.pack(side=tk.TOP)
        close_button.pack(side=tk.BOTTOM)

        # victory handling
        claim_button = tk.Button(self.root, text="Claim Victory", command=lambda: self.claim_victory(claim_direction_dropdown.get(), claim_location_dropdown.get(), claim_characteristic_dropdown.get()))

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

    def draw_board(self) -> None:
        """draws all pieces and board"""
        self.draw_piece("lpss", 250, 75)
        self.piece_played["lpss"] = False
        self.draw_piece("lpsc", 250, 305)
        self.piece_played["lpsc"] = False
        self.draw_piece("spss", 275, 535)
        self.piece_played["spss"] = False
        self.draw_piece("spsc", 275, 665)
        self.piece_played["spsc"] = False
        self.draw_piece("lphs", 250, 190)
        self.piece_played["lphs"] = False
        self.draw_piece("lphc", 250, 420)
        self.piece_played["lphc"] = False
        self.draw_piece("sphs", 275, 600)
        self.piece_played["sphs"] = False
        self.draw_piece("sphc", 275, 730)
        self.piece_played["sphc"] = False
        self.draw_piece("lgss", 50, 75)
        self.piece_played["lgss"] = False
        self.draw_piece("lgsc", 50, 305)
        self.piece_played["lgsc"] = False
        self.draw_piece("sgss", 75, 535)
        self.piece_played["sgss"] = False
        self.draw_piece("sgsc", 75, 665)
        self.piece_played["sgsc"] = False
        self.draw_piece("lghs", 50, 190)
        self.piece_played["lghs"] = False
        self.draw_piece("lghc", 50, 420)
        self.piece_played["lghc"] = False
        self.draw_piece("sghs", 75, 600)
        self.piece_played["sghs"] = False
        self.draw_piece("sghc", 75, 730)
        self.piece_played["sghc"] = False

        # have to draw 16 rectangles instead of lines in order to highlight them upon mouseover
        for i in range(4):
            for j in range(4):
                # instead of 200, use 202 to create 2px extra space between squares so highlight doesn't overlap
                id = self.canvas.create_rectangle(400 + 202 * i, 50 + 202 * j, 600 + 202 * i, 250 + 202 * j, fill="white", outline="black", width=1)
                self.canvas.addtag_withtag(f"board-{i}-{j}", id)

    def select_piece(self, event, tag):
        """Selects a piece if clicked."""
        if self.state == "Player 1 Places" or self.state == "Player 2 Places":
            print(f"Invalid action for state: {self.state}")
            return
        
        if self.piece_played[tag]:
            print(f"Piece {tag} has already been played!")
        else:
            self.selected_piece = tag
            print(f"Piece selected: {self.selected_piece}")
            self.change_turn()
        
        self._click_highlight(event, tag)  # Highlight the selected piece on click

    def place_piece(self, event, tag):
        """Places a selected piece on an empty grid slot."""
        if self.state == "Player 1 Selects" or self.state == "Player 2 Selects":
            print(f"Invalid action for state: {self.state}")
            return

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
                self.canvas.itemconfig(self.selected_piece, outline="black", width=1)  # Reset outline color and width
                self.selected_piece = None
                self.change_turn()
            else:
                print("Error: Could not get selected piece coordinates!")
        else:
            print(f"Slot ({i}, {j}) is already occupied!")

    ### WINNING CONDITIONS FUNCTIONS ###

    def _check_win_row(self, row: int, characteristic: str) -> bool:
        """
        Checks for a win in a row based on a characteristic.

        Args:
            row (int): Row index.
            characteristic (str): "size", "color", "fill", or "shape".

        Returns:
            bool: True if there's a win, False otherwise.
        """
        # size, color, fill, shape
        total_scores = [0, 0, 0, 0]
        current_categories = [None, None, None, None]

        for col in range(4):
            if self.board[row][col] is None:
                continue
            else:
                tag = self.canvas.gettags(self.board[row][col])[0]

                total_scores, current_categories = self._check_win_tag_identifier(total_scores, current_categories, tag)

                # print(f"check win {tag} at ({row},{col}) count_size: {total_scores[0]}, count_color: {total_scores[1]}, count_fill: {total_scores[2]}, count_shape: {total_scores[3]}")

            if (total_scores[0] == 4 and characteristic == "size") or (total_scores[1] == 4 and characteristic == "color") or (total_scores[2] == 4 and characteristic == "fill") or (total_scores[3] == 4 and characteristic == "shape"):
                return True
        return False

    def _check_win_col(self, col: int, characteristic: str) -> bool:
        """
        Checks for a win in a col based on a characteristic.

        Args:
            col (int): The column index to check for a win
            characteristic (str): The characteristic to check for a win. Can be "size", "color", "fill", or "shape".

        Returns:
            bool: True if there is a win based on the specified characteristic, False otherwise.
        """
        # size, color, fill, shape
        total_scores = [0, 0, 0, 0]
        current_categories = [None, None, None, None]

        for row in range(4):
            if self.board[row][col] is None:
                continue
            else:
                tag = self.canvas.gettags(self.board[row][col])[0]

                total_scores, current_categories = self._check_win_tag_identifier(total_scores, current_categories, tag)

                # print(f"check win {tag} at ({row},{col}) count_size: {total_scores[0]}, count_color: {total_scores[1]}, count_fill: {total_scores[2]}, count_shape: {total_scores[3]}")

            if (total_scores[0] == 4 and characteristic == "size") or (total_scores[1] == 4 and characteristic == "color") or (total_scores[2] == 4 and characteristic == "fill") or (total_scores[3] == 4 and characteristic == "shape"):
                return True
        return False

    def _check_win_diagonal(self, diagonal: str, characteristic: str) -> bool:
        """
        Checks if there is a winning condition on the specified diagonal.
        Args:
            diagonal (str): The diagonal to check, either "main" or "anti".
            characteristic (str): The characteristic to check for a win, can be "size", "color", "fill", or "shape".
        Returns:
            bool: True if there is a winning condition on the specified diagonal, False otherwise.
        """
        total_scores = [0, 0, 0, 0]
        current_categories = [None, None, None, None]

        main = [(0, 0), (1, 1), (2, 2), (3, 3)]
        anti = [(3, 0), (2, 1), (1, 2), (0, 3)]
        if diagonal == "main":
            for row, col in main:
                if self.board[row][col] is None:
                    continue
                else:
                    tag = self.canvas.gettags(self.board[row][col])[0]

                    total_scores, current_categories = self._check_win_tag_identifier(total_scores, current_categories, tag)

                    # print(f"check win {tag} at ({row},{col}) count_size: {total_scores[0]}, count_color: {total_scores[1]}, count_fill: {total_scores[2]}, count_shape: {total_scores[3]}")

            if (total_scores[0] == 4 and characteristic == "size") or (total_scores[1] == 4 and characteristic == "color") or (total_scores[2] == 4 and characteristic == "fill") or (total_scores[3] == 4 and characteristic == "shape"):
                return True
        if diagonal == "anti":
            for row, col in anti:
                if self.board[row][col] is None:
                    continue
                else:
                    tag = self.canvas.gettags(self.board[row][col])[0]

                    total_scores, current_categories = self._check_win_tag_identifier(total_scores, current_categories, tag)

                    # print(f"check win {tag} at ({row},{col}) count_size: {total_scores[0]}, count_color: {total_scores[1]}, count_fill: {total_scores[2]}, count_shape: {total_scores[3]}")

            if (total_scores[0] == 4 and characteristic == "size") or (total_scores[1] == 4 and characteristic == "color") or (total_scores[2] == 4 and characteristic == "fill") or (total_scores[3] == 4 and characteristic == "shape"):
                return True
            return False

    def _check_win_tag_identifier(self, total_scores: list[int], current_categories: list[str], tag: list[str]) -> list[list[int], list[str]]:
        """
        checks to see if the tag matches the current category and updates the total scores and current categories accordingly
        Parameters:
          total_scores: list[int] - the list of total scores for each category
          current_categories: list[str] - the list of current categories for each category (size, color, fill, shape)
          tag: list[str] - the tag to check against the current categories
        Returns:
          total_scores: list[int] - the updated list of total scores for each category
          current_categories: list[str] - the updated list of current categories for each category
        """
        if tag[0] == current_categories[0]:  # if size
            total_scores[0] += 1
        else:
            total_scores[0] = 1
            current_categories[0] = tag[0]

        if tag[1] == current_categories[1]:  # if color
            total_scores[1] += 1
        else:
            total_scores[1] = 1
            current_categories[1] = tag[1]

        if tag[2] == current_categories[2]:  # if fill
            total_scores[2] += 1
        else:
            total_scores[2] = 1
            current_categories[2] = tag[2]

        if tag[3] == current_categories[3]:  # if shape
            total_scores[3] += 1
        else:
            total_scores[3] = 1
            current_categories[3] = tag[3]
        return total_scores, current_categories

    def check_win_any(self):
        """
        Checks if a player has won in any row, column, or diagonal.
        Returns True if any winning condition is met.
        """
        characteristic = ["size", "color", "fill", "shape"]
        for c in characteristic:
            for row in range(4):
                if self.claim_victory("row", row + 1, c):
                    return

            for col in range(4):
                if self.claim_victory("column", col + 1, c):
                    return

            if self.claim_victory("diagonal", "main", c):
                return

            if self.claim_victory("diagonal", "anti", c):
                return

    def claim_victory(self, claim_direction: str, claim_location: str, claim_characteristic: str):
        """
        Claims victory and highlights the winning pieces.

        This method checks if there is a winning condition based on the claim type, location, and characteristic provided.
        If a winning condition is met, it announces the winner and highlights the winning pieces.

        Parameters:
        claim_direction_entry (str): The type of claim ("row", "column", or "diagonal").
        claim_location_entry (str): The location of the claim (row number, column number, or diagonal type).
        claim_characteristic_entry (str): The characteristic of the claim ("size", "color", "fill", or "shape").
        """
        is_win = None
        if claim_direction == "diagonal":
            is_win = self._check_win_diagonal(claim_location, claim_characteristic)
        else:
            if claim_direction == "row":
                is_win = self._check_win_row(int(claim_location) - 1, claim_characteristic)
            elif claim_direction == "column":
                is_win = self._check_win_col(int(claim_location) - 1, claim_characteristic)

        if is_win:
            print(f"Player {''.join(self.state.split(' ')[0:2])} wins!")
            messagebox.showinfo("Game Over", f"Player {''.join(self.state.split(' ')[0:2])} wins!")
            return True
        
        print("No winner yet!")
        return False


    ### TKINTER DYNAMIC UPDATE FUNCTIONS ###
    def handle_bot_place(self):
        """Handles the bot's turn if player 2 is a bot. It selects a piece and places it on the board."""
        # Find a spot for the bot's move
        i, j = self.bot.place_piece(self.board, self.piece_played, self.selected_piece)
        self.place_piece(None, f"board-{i}-{j}")  # Simulate click on the board spot
        self.check_win_any()
    
    def handle_bot_select(self):
        """Handles the bot's selection of a piece to play.
        This function is called when it's the bot's turn to select a piece.
        """
        selected_piece = self.bot.select_piece(self.board, self.piece_played)
        if selected_piece:
            # "clicks" the piece by generating a click event at the center of the piece
            # button click automatically handles changing the turn
            coords = self.canvas.coords(selected_piece)
            self.canvas.event_generate("<Button-1>", x=(coords[0] + coords[2]) / 2, y=(coords[1] + coords[3]) / 2)
            self.selected_piece = selected_piece 

    def change_turn(self):
        """Changes turn and updates the display correctly"""
        state_index = self.possible_states.index(self.state)
        # goes back to the first index if at the last state
        state_index = 0 if state_index + 1 >= len(self.possible_states) else state_index + 1
        self.state = self.possible_states[state_index]

        self.player_display.config(text=f"{self.state}", fg="seagreen" if self.state.startswith("Player 1") else "purple4")
        
        if self.bot:
            if self.state == "Player 2 Places":
                self.root.after(500, self.handle_bot_place)  # Ensure delay before bot plays
            elif self.state == "Player 2 Selects":
                self.root.after(500, self.handle_bot_select)

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

    def _highlight(self, event, id):
        """change border color to yellow and increase width of border upon mouseover.
        Doesn't highlight if the piece is already selected.
        """
        tag = self.canvas.gettags(id)[0]
        if tag == self.selected_piece:
            return
        self.canvas.itemconfig(id, outline="yellow", width=3)

    def _unhighlight(self, event, id):
        """change border color to black and increase width of border upon mouseover.
        Doesn't unhighlight if the piece is already selected.
        """
        tag = self.canvas.gettags(id)[0]
        if tag == self.selected_piece:
            return
        self.canvas.itemconfig(id, outline="black", width=1)

    def _click_highlight(self, event, tag):
        """change border color to red and increase width of border upon mouse click.
        Overrides the highlight and unhighlight functions.
        """
        self.canvas.itemconfig(tag, outline="red", width=3)

    ### TKINTER BIND FUNCTIONS ###

    def _bind_highlight(self):
        """binds the highlight and unhighlight functions to all tags"""
        all_tags = []
        for id in self.canvas.find_all():
            tags = self.canvas.gettags(id)
            all_tags += tags

        for tag in all_tags:
            ids = self.canvas.find_withtag(tag)
            self.canvas.tag_bind(ids[0], "<Enter>", lambda event, id=ids[0]: self._highlight(event, id))
            self.canvas.tag_bind(ids[0], "<Leave>", lambda event, id=ids[0]: self._unhighlight(event, id))
            if len(ids) > 1:
                # only for hollow pieces, ensures that hovering over either the inner or outer piece will highlight both
                self.canvas.tag_bind(
                    ids[1],
                    "<Enter>",
                    lambda event, id=ids[0]: self._highlight(event, id),
                )
                self.canvas.tag_bind(
                    ids[1],
                    "<Leave>",
                    lambda event, id=ids[0]: self._unhighlight(event, id),
                )

    def _bind_clicks(self):
        """Binds mouse clicks for selecting and placing pieces."""
        for id in self.canvas.find_all():
            tags = self.canvas.gettags(id)
            if tags and not tags[0].startswith("board-") and not tags[0].startswith("category-"):
                # Bind piece selection to the first tag of the piece
                self.canvas.tag_bind(
                    tags[0],
                    "<Button-1>",
                    lambda event, tag=tags[0]: self.select_piece(event, tag),
                )
            elif tags and tags[0].startswith("board-") and not tags[0].startswith("category-"):
                # Bind grid slot placement
                self.canvas.tag_bind(
                    tags[0],
                    "<Button-1>",
                    lambda event, tag=tags[0]: self.place_piece(event, tag),
                )

    ### DRAW SHAPE AND ASSIGN TAGS FUNCTIONS ###

    def _draw_large_purple_solid_square(self, startx: int, starty: int) -> None:
        id = self.canvas.create_rectangle(startx, starty, startx + self.large_large, starty + self.large_large, fill="purple4")
        self.canvas.addtag_withtag("lpss", id)

    def _draw_large_purple_hollow_square(self, startx: int, starty: int) -> None:
        id1 = self.canvas.create_rectangle(startx, starty, startx + self.large_large, starty + self.large_large, fill="purple4")
        id2 = self.canvas.create_rectangle(startx + self.large_small, starty + self.large_small, startx + self.large_large - self.large_small, starty + self.large_large - self.large_small, outline="purple4", fill="mediumpurple1")
        self.canvas.addtag_withtag("lphs", id1)
        self.canvas.addtag_withtag("lphs", id2)

    def _draw_large_purple_solid_circle(self, startx: int, starty: int) -> None:
        id = self.canvas.create_oval(startx, starty, startx + self.large_large, starty + self.large_large, fill="purple4")
        self.canvas.addtag_withtag("lpsc", id)

    def _draw_large_purple_hollow_circle(self, startx: int, starty: int) -> None:
        id1 = self.canvas.create_oval(startx, starty, startx + self.large_large, starty + self.large_large, fill="purple4", outline="purple4", width=2)
        id2 = self.canvas.create_oval(startx + self.large_small, starty + self.large_small, startx + self.large_large - self.large_small, starty + self.large_large - self.large_small, fill="mediumpurple1", outline="purple4", width=2)
        self.canvas.addtag_withtag("lphc", id1)
        self.canvas.addtag_withtag("lphc", id2)

    def _draw_small_purple_solid_square(self, startx: int, starty: int) -> None:
        id = self.canvas.create_rectangle(startx, starty, startx + self.small_large, starty + self.small_large, fill="purple4")
        self.canvas.addtag_withtag("spss", id)

    def _draw_small_purple_hollow_square(self, startx: int, starty: int) -> None:
        id1 = self.canvas.create_rectangle(startx, starty, startx + self.small_large, starty + self.small_large, fill="purple4")
        id2 = self.canvas.create_rectangle(startx + self.small_small, starty + self.small_small, startx + self.small_large - self.small_small, starty + self.small_large - self.small_small, outline="purple4", fill="mediumpurple1")
        self.canvas.addtag_withtag("sphs", id1)
        self.canvas.addtag_withtag("sphs", id2)

    def _draw_small_purple_solid_circle(self, startx: int, starty: int) -> None:
        id = self.canvas.create_oval(startx, starty, startx + self.small_large, starty + self.small_large, fill="purple4")
        self.canvas.addtag_withtag("spsc", id)

    def _draw_small_purple_hollow_circle(self, startx: int, starty: int) -> None:
        id1 = self.canvas.create_oval(startx, starty, startx + self.small_large, starty + self.small_large, fill="purple4", outline="purple4", width=2)
        id2 = self.canvas.create_oval(startx + self.small_small, starty + self.small_small, startx + self.small_large - self.small_small, starty + self.small_large - self.small_small, fill="mediumpurple1", outline="purple4", width=2)
        self.canvas.addtag_withtag("sphc", id1)
        self.canvas.addtag_withtag("sphc", id2)

    def _draw_large_green_solid_square(self, startx: int, starty: int) -> None:
        id = self.canvas.create_rectangle(startx, starty, startx + self.large_large, starty + self.large_large, fill="seagreen")
        self.canvas.addtag_withtag("lgss", id)

    def _draw_large_green_hollow_square(self, startx: int, starty: int) -> None:
        id1 = self.canvas.create_rectangle(startx, starty, startx + self.large_large, starty + self.large_large, fill="seagreen")
        id2 = self.canvas.create_rectangle(startx + self.large_small, starty + self.large_small, startx + self.large_large - self.large_small, starty + self.large_large - self.large_small, outline="seagreen", fill="mediumseagreen")
        self.canvas.addtag_withtag("lghs", id1)
        self.canvas.addtag_withtag("lghs", id2)

    def _draw_large_green_solid_circle(self, startx: int, starty: int) -> None:
        id = self.canvas.create_oval(startx, starty, startx + self.large_large, starty + self.large_large, fill="seagreen")
        self.canvas.addtag_withtag("lgsc", id)

    def _draw_large_green_hollow_circle(self, startx: int, starty: int) -> None:
        id1 = self.canvas.create_oval(startx, starty, startx + self.large_large, starty + self.large_large, fill="seagreen", outline="seagreen", width=2)
        id2 = self.canvas.create_oval(startx + self.large_small, starty + self.large_small, startx + self.large_large - self.large_small, starty + self.large_large - self.large_small, fill="mediumseagreen", outline="seagreen", width=2)
        self.canvas.addtag_withtag("lghc", id1)
        self.canvas.addtag_withtag("lghc", id2)

    def _draw_small_green_solid_square(self, startx: int, starty: int) -> None:
        id = self.canvas.create_rectangle(startx, starty, startx + self.small_large, starty + self.small_large, fill="seagreen")
        self.canvas.addtag_withtag("sgss", id)

    def _draw_small_green_hollow_square(self, startx: int, starty: int) -> None:
        id1 = self.canvas.create_rectangle(startx, starty, startx + self.small_large, starty + self.small_large, fill="seagreen")
        id2 = self.canvas.create_rectangle(startx + self.small_small, starty + self.small_small, startx + self.small_large - self.small_small, starty + self.small_large - self.small_small, outline="seagreen", fill="mediumseagreen")
        self.canvas.addtag_withtag("sghs", id1)
        self.canvas.addtag_withtag("sghs", id2)

    def _draw_small_green_solid_circle(self, startx: int, starty: int) -> None:
        id = self.canvas.create_oval(startx, starty, startx + self.small_large, starty + self.small_large, fill="seagreen")
        self.canvas.addtag_withtag("sgsc", id)

    def _draw_small_green_hollow_circle(self, startx: int, starty: int) -> None:
        id1 = self.canvas.create_oval(startx, starty, startx + self.small_large, starty + self.small_large, fill="seagreen", outline="seagreen", width=2)
        id2 = self.canvas.create_oval(startx + self.small_small, starty + self.small_small, startx + self.small_large - self.small_small, starty + self.small_large - self.small_small, fill="mediumseagreen", outline="seagreen", width=2)
        self.canvas.addtag_withtag("sghc", id1)
        self.canvas.addtag_withtag("sghc", id2)
        self.canvas.addtag_withtag("sghc", id2)

    def draw_piece(self, piece: str, startx: int, starty: int) -> None:
        """lookup dictionary function to draw a piece based on its name"""
        piece_functions = {
            "lpss": self._draw_large_purple_solid_square,
            "spss": self._draw_small_purple_solid_square,
            "lphs": self._draw_large_purple_hollow_square,
            "sphc": self._draw_small_purple_hollow_circle,
            "lpsc": self._draw_large_purple_solid_circle,
            "sgsc": self._draw_small_green_solid_circle,
            "spsc": self._draw_small_purple_solid_circle,
            "lghc": self._draw_large_green_hollow_circle,
            "lphc": self._draw_large_purple_hollow_circle,
            "sghc": self._draw_small_green_hollow_circle,
            "sphs": self._draw_small_purple_hollow_square,
            "lgss": self._draw_large_green_solid_square,
            "sgss": self._draw_small_green_solid_square,
            "lghs": self._draw_large_green_hollow_square,
            "sghs": self._draw_small_green_hollow_square,
            "lgsc": self._draw_large_green_solid_circle,
        }
        if piece in piece_functions:
            piece_functions[piece](startx, starty)
        else:
            print(f"Error: Unknown piece name '{piece}'")


q = Quarto()