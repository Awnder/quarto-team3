import tkinter as tk
import tkinter.ttk

class Quarto:
  def __init__(self):
    # initalize menu and game tk screens
    self.root = None
    self.canvas = None
    self.board = None

    # players
    self.player1 = None
    self.player2 = None
    self.turn = None
    self.player_display = None

    # pieces
    self.small_small = 15
    self.small_large = 50
    self.large_small = 25
    self.large_large = 100
    self.selected_piece = None  # Stores the currently selected piece's tag
    self.piece_played = {}

    self.init_menu_screen() # start game here at menu

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
    self.root.configure(bg = "black")

    player1_name = tk.StringVar()
    player2_name = tk.StringVar()

    title = tk.Label(self.root, text="Welcome to Quarto", font=('Courier', 25, 'bold'), bg="black")
    instruction = tk.Label(self.root, text="Enter Player Names to Begin!", font=('Courier', 15, 'normal'), bg="black")

    player1_name_label = tk.Label(self.root, text="Player 1 Name", font=('Courier', 15, 'bold'), fg="seagreen", bg="black")
    player2_name_label = tk.Label(self.root, text="Player 2 Name", font=('Courier', 15, 'bold'), fg="purple4", bg="black")

    player1_name_entry = tk.Entry(self.root, textvariable=player1_name, font=('Courier', 12, 'normal'), fg="seagreen", bg="grey")
    player2_name_entry = tk.Entry(self.root, textvariable=player2_name, font=('Courier', 12, 'normal'), fg="purple4", bg="grey")

    submit_button = tk.Button(self.root, text="Start Game", command=lambda: self.init_game_screen(player1_name, player2_name), bg="grey")

    title.pack(pady=20)
    instruction.pack()
    player1_name_label.pack(pady=25)
    player1_name_entry.pack()
    player2_name_label.pack(pady=25)
    player2_name_entry.pack()
    submit_button.pack(pady=10)
  
  def init_game_screen(self, player1_name: tk.StringVar, player2_name: tk.StringVar):
    """ 
    creates a game screen so players can play quarto 
    the goal is upon game end, tkinter will juggle between the menu and gameboard screen 
    """
    if self.root:
      self.root.destroy()

    # recreate tk interface for the game board
    self.root = tk.Tk()
    self.root.title('Quarto Game')
    self.root.geometry('2400x1600')
    self.canvas = tk.Canvas(self.root)
    self.canvas.pack(fill=tk.BOTH, expand=1)
    self.canvas.configure(bg="white")

    # if player name is empty just default to Player 1 or Player 2
    if player1_name.get().strip() == "":
      self.player1 = 'Player 1'
    else:
      self.player1 = player1_name.get()
    if player2_name.get().strip() == "":
      self.player2 = 'Player 2'
    else:
      self.player2 = player2_name.get()
    self.turn = self.player1

    self.draw_board()
    self.bind_highlight()
    self.bind_clicks()
    self.board = [[None for _ in range(4)] for _ in range(4)] # creates a list of lists with 4 rows and 4 columns to fill in with pieces
    
    self.player_display = tk.Label(self.root, text=f"{self.turn}'s Turn", font=('Courier', 15, 'bold'), fg="seagreen")
    close_button = tk.Button(self.root, text="Close", command=self.init_menu_screen)
    self.player_display.pack(side=tk.TOP)    
    close_button.pack(side=tk.BOTTOM)
    self.claim_button = tk.Button(self.root, text="Claim Victory", command=self.claim_victory)
    self.claim_button.pack(side=tk.RIGHT)

  def change_turn(self):
    """ changes color, turn, and player display on each turn """
    color = "purple4" if self.turn == self.player1 else "seagreen"
    self.turn = self.player1 if self.turn == self.player2 else self.player2
    self.player_display.config(text=f"{self.turn}'s Turn", fg=color)

  def draw_board(self) -> None:
    ''' draws all pieces and board '''
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
    
  def bind_highlight(self):
    ''' binds the highlight and unhighlight functions to all tags '''
    all_tags = []
    for id in self.canvas.find_all():
      tags = self.canvas.gettags(id)
      all_tags += tags
    
    for tag in all_tags:
      ids = self.canvas.find_withtag(tag)
      self.canvas.tag_bind(ids[0], "<Enter>", lambda event, id=ids[0]: self.highlight(event, id))
      self.canvas.tag_bind(ids[0], "<Leave>", lambda event, id=ids[0]: self.unhighlight(event, id))
      if len(ids) > 1: # only for hollow pieces, ensures that hovering over either the inner or outer piece will highlight both
        self.canvas.tag_bind(ids[1], "<Enter>", lambda event, id=ids[0]: self.highlight(event, id))
        self.canvas.tag_bind(ids[1], "<Leave>", lambda event, id=ids[0]: self.unhighlight(event, id))
    
  def bind_clicks(self):
    ''' Binds mouse clicks for selecting and placing pieces. '''
    for id in self.canvas.find_all():
        tags = self.canvas.gettags(id)
        if tags and not tags[0].startswith("board-") and not tags[0].startswith("category-"):
            # Bind piece selection to the first tag of the piece
            self.canvas.tag_bind(tags[0], "<Button-1>", lambda event, tag=tags[0]: self.select_piece(event, tag))
        elif tags and tags[0].startswith("board-") and not tags[0].startswith("category-"):
            # Bind grid slot placement
            self.canvas.tag_bind(tags[0], "<Button-1>", lambda event, tag=tags[0]: self.place_piece(event, tag))
  
  def select_piece(self, event, tag):
    ''' Selects a piece if clicked. '''
    if self.piece_played[tag]:
      print(f"Piece {tag} has already been played!")
    else:
      self.selected_piece = tag
      print(f"Piece selected: {self.selected_piece}")
        
  def place_piece(self, event, tag):
    ''' Places a selected piece on an empty grid slot. '''
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

    self.change_turn()    

  def _check_win_row(self, row: int) -> bool:
    """ iterates through a given row to check for a win. returns True if there is a win, False otherwise """
    # size, color, fill, shape
    total_scores = [0, 0, 0, 0]
    current_categories = [None, None, None, None]

    for col in range(4):
      if self.board[row][col] is None: 
        continue
      else:
        tag = self.canvas.gettags(self.board[row][col])[0]

        total_scores, current_categories = self._check_win_tag_identifier(total_scores, current_categories, tag)

        print(f'check win {tag} at ({row},{col}) count_size: {total_scores[0]}, count_color: {total_scores[1]}, count_fill: {total_scores[2]}, count_shape: {total_scores[3]}')

      if total_scores[0] == 4 or total_scores[1] == 4 or total_scores[2] == 4 or total_scores[3] == 4:
        return True
    return False

  def _check_win_col(self, col: int) -> bool:
    """ iterates through a given column to check for a win. returns True if there is a win, False otherwise """
    # size, color, fill, shape
    total_scores = [0, 0, 0, 0]
    current_categories = [None, None, None, None]

    for row in range(4):
      if self.board[row][col] is None:
        continue
      else:
        tag = self.canvas.gettags(self.board[row][col])[0]

        total_scores, current_categories = self._check_win_tag_identifier(total_scores, current_categories, tag)

        print(f'check win {tag} at ({row},{col}) count_size: {total_scores[0]}, count_color: {total_scores[1]}, count_fill: {total_scores[2]}, count_shape: {total_scores[3]}')

      if total_scores[0] == 4 or total_scores[1] == 4 or total_scores[2] == 4 or total_scores[3] == 4:
        return True
    return False
  
  def _check_win_diagonal(self, diagonal: str) -> bool:
    total_scores = [0, 0, 0, 0]
    current_categories = [None, None, None, None]

    main = [(0, 0), (1, 1), (2,2), (3, 3)]
    anti = [(3, 0), (2, 1), (1, 2), (0, 3)]
    if diagonal == 'main':
      for row, col in main:
        if self.board[row][col] is None:
          continue
        else:
          tag = self.canvas.gettags(self.board[row][col])[0]

          total_scores, current_categories = self._check_win_tag_identifier(total_scores, current_categories, tag)

          print(f'check win {tag} at ({row},{col}) count_size: {total_scores[0]}, count_color: {total_scores[1]}, count_fill: {total_scores[2]}, count_shape: {total_scores[3]}')

      if total_scores[0] == 4 or total_scores[1] == 4 or total_scores[2] == 4 or total_scores[3] == 4:
        return True
    if diagonal == 'anti':
      for row, col in anti:
        if self.board[row][col] is None:
          continue
        else:
          tag = self.canvas.gettags(self.board[row][col])[0]

          total_scores, current_categories = self._check_win_tag_identifier(total_scores, current_categories, tag)

          print(f'check win {tag} at ({row},{col}) count_size: {total_scores[0]}, count_color: {total_scores[1]}, count_fill: {total_scores[2]}, count_shape: {total_scores[3]}')

      if total_scores[0] == 4 or total_scores[1] == 4 or total_scores[2] == 4 or total_scores[3] == 4:
        return True
      return False



  def _check_win_tag_identifier(self, total_scores: list[int], current_categories: list[str], tag: list[str]) -> list[list[int], list[str]]:
    """ 
    checks to see if the tag matches the current category and updates the total scores and current categories accordingly 
    Parameters:
      total_scores: list[int] - the list of total scores for each category
      current_categories: list[str] - the list of current categories for each category
      tag: list[str] - the tag to check against the current categories
    Returns:
      total_scores: list[int] - the updated list of total scores for each category
      current_categories: list[str] - the updated list of current categories for each category
    """
    if tag[0] == current_categories[0]:
      total_scores[0] += 1
    else:
      total_scores[0] = 1
      current_categories[0] = tag[0]

    if tag[1] == current_categories[1]:
      total_scores[1] += 1
    else:
      total_scores[1] = 1
      current_categories[1] = tag[1]

    if tag[2] == current_categories[2]:
      total_scores[2] += 1
    else:
      total_scores[2] = 1
      current_categories[2] = tag[2]

    if tag[3] == current_categories[3]:
      total_scores[3] += 1
    else:
      total_scores[3] = 1
      current_categories[3] = tag[3]
    return total_scores, current_categories
    
  def _check_win_wrapper(self, row=None, col=None, diagonal=None) -> bool:
    """
    Wrapper function to check if a player has won based on the given row, column, or diagonal.
    At least one of row, col, or diagonal should be specified.
    """
    if row is not None:
        return self._check_win_row(row)
    if col is not None:
        return self._check_win_col(col)
    if diagonal is not None:
        return self._check_win_diagonal(diagonal)

    return False

  def _check_win_any(self) -> bool:
    """
    Checks if a player has won in any row, column, or diagonal.
    Returns True if any winning condition is met.
    """
    for row in range(4):
        if self._check_win_row(row):
            return True

    for col in range(4):
        if self._check_win_col(col):
            return True

    if self._check_win_diagonal("main") or self._check_win_diagonal("anti"):
        return True

    return False

  def claim_victory(self):
    ''' Claims victory and highlights the winning pieces '''
    winner, winning_pieces = self._check_win_any()

    if winner:
        print(f"Player {winner} wins!")
        for piece in winning_pieces:
            piece_id = self.get_piece_id(piece)
            self.highlight(piece_id)

        self.display_victory_message(winner)
    else:
        print("No winner yet!")

  def highlight(self, event, id):
    ''' change border color to yellow and increase width of border upon mouseover '''
    self.canvas.itemconfig(id, outline="yellow", width=3)

  def unhighlight(self, event, id):
    ''' change border color to black and increase width of border upon mouseover '''
    self.canvas.itemconfig(id, outline="black", width=1)

  def draw_large_purple_solid_square(self, startx: int, starty: int) -> None:
    id = self.canvas.create_rectangle(startx, starty, startx+self.large_large, starty+self.large_large, fill="purple4")
    self.canvas.addtag_withtag("lpss", id)

  def draw_large_purple_hollow_square(self, startx: int, starty: int) -> None:
    id1 = self.canvas.create_rectangle(startx, starty, startx+self.large_large, starty+self.large_large, fill="purple4")
    id2 = self.canvas.create_rectangle(startx+self.large_small, starty+self.large_small, startx+self.large_large-self.large_small, starty+self.large_large-self.large_small, outline="purple4", fill="mediumpurple1")
    self.canvas.addtag_withtag("lphs", id1)
    self.canvas.addtag_withtag("lphs", id2)

  def draw_large_purple_solid_circle(self, startx: int, starty: int) -> None:
    id = self.canvas.create_oval(startx, starty, startx+self.large_large, starty+self.large_large, fill="purple4")
    self.canvas.addtag_withtag("lpsc", id)

  def draw_large_purple_hollow_circle(self, startx: int, starty: int) -> None:
    id1 = self.canvas.create_oval(startx, starty, startx+self.large_large, starty+self.large_large, fill="purple4", outline="purple4", width=2)
    id2 = self.canvas.create_oval(startx+self.large_small, starty+self.large_small, startx+self.large_large-self.large_small, starty+self.large_large-self.large_small, fill="mediumpurple1", outline="purple4", width=2)
    self.canvas.addtag_withtag("lphc", id1)
    self.canvas.addtag_withtag("lphc", id2)

  def draw_small_purple_solid_square(self, startx: int, starty: int) -> None:
    id = self.canvas.create_rectangle(startx, starty, startx+self.small_large, starty+self.small_large, fill="purple4")
    self.canvas.addtag_withtag("spss", id)

  def draw_small_purple_hollow_square(self, startx: int, starty: int) -> None:
    id1 = self.canvas.create_rectangle(startx, starty, startx+self.small_large, starty+self.small_large, fill="purple4")
    id2 = self.canvas.create_rectangle(startx+self.small_small, starty+self.small_small, startx+self.small_large-self.small_small, starty+self.small_large-self.small_small, outline="purple4", fill="mediumpurple1")
    self.canvas.addtag_withtag("sphs", id1)
    self.canvas.addtag_withtag("sphs", id2)

  def draw_small_purple_solid_circle(self, startx: int, starty: int) -> None:
    id = self.canvas.create_oval(startx, starty, startx+self.small_large, starty+self.small_large, fill="purple4")
    self.canvas.addtag_withtag("spsc", id)

  def draw_small_purple_hollow_circle(self, startx: int, starty: int) -> None:
    id1 = self.canvas.create_oval(startx, starty, startx+self.small_large, starty+self.small_large, fill="purple4", outline="purple4", width=2)
    id2 = self.canvas.create_oval(startx+self.small_small, starty+self.small_small, startx+self.small_large-self.small_small, starty+self.small_large-self.small_small, fill="mediumpurple1", outline="purple4", width=2)
    self.canvas.addtag_withtag("sphc", id1)
    self.canvas.addtag_withtag("sphc", id2)

  def draw_large_green_solid_square(self, startx: int, starty: int) -> None:
    id = self.canvas.create_rectangle(startx, starty, startx+self.large_large, starty+self.large_large, fill="seagreen")
    self.canvas.addtag_withtag("lgss", id)

  def draw_large_green_hollow_square(self, startx: int, starty: int) -> None:
    id1 = self.canvas.create_rectangle(startx, starty, startx+self.large_large, starty+self.large_large, fill="seagreen")
    id2 = self.canvas.create_rectangle(startx+self.large_small, starty+self.large_small, startx+self.large_large-self.large_small, starty+self.large_large-self.large_small, outline="seagreen", fill="mediumseagreen")
    self.canvas.addtag_withtag("lghs", id1)
    self.canvas.addtag_withtag("lghs", id2)

  def draw_large_green_solid_circle(self, startx: int, starty: int) -> None:
    id = self.canvas.create_oval(startx, starty, startx+self.large_large, starty+self.large_large, fill="seagreen")
    self.canvas.addtag_withtag("lgsc", id)

  def draw_large_green_hollow_circle(self, startx: int, starty: int) -> None:
    id1 = self.canvas.create_oval(startx, starty, startx+self.large_large, starty+self.large_large, fill="seagreen", outline="seagreen", width=2)
    id2 = self.canvas.create_oval(startx+self.large_small, starty+self.large_small, startx+self.large_large-self.large_small, starty+self.large_large-self.large_small, fill="mediumseagreen", outline="seagreen", width=2)
    self.canvas.addtag_withtag("lghc", id1)
    self.canvas.addtag_withtag("lghc", id2)

  def draw_small_green_solid_square(self, startx: int, starty: int) -> None:
    id = self.canvas.create_rectangle(startx, starty, startx+self.small_large, starty+self.small_large, fill="seagreen")
    self.canvas.addtag_withtag("sgss", id)

  def draw_small_green_hollow_square(self, startx: int, starty: int) -> None:
    id1 = self.canvas.create_rectangle(startx, starty, startx+self.small_large, starty+self.small_large, fill="seagreen")
    id2 = self.canvas.create_rectangle(startx+self.small_small, starty+self.small_small, startx+self.small_large-self.small_small, starty+self.small_large-self.small_small, outline="seagreen", fill="mediumseagreen")
    self.canvas.addtag_withtag("sghs", id1)
    self.canvas.addtag_withtag("sghs", id2)

  def draw_small_green_solid_circle(self, startx: int, starty: int) -> None:
    id = self.canvas.create_oval(startx, starty, startx+self.small_large, starty+self.small_large, fill="seagreen")
    self.canvas.addtag_withtag("sgsc", id)

  def draw_small_green_hollow_circle(self, startx: int, starty: int) -> None:
    id1 = self.canvas.create_oval(startx, starty, startx+self.small_large, starty+self.small_large, fill="seagreen", outline="seagreen", width=2)
    id2 = self.canvas.create_oval(startx+self.small_small, starty+self.small_small, startx+self.small_large-self.small_small, starty+self.small_large-self.small_small, fill="mediumseagreen", outline="seagreen", width=2)
    self.canvas.addtag_withtag("sghc", id1)
    self.canvas.addtag_withtag("sghc", id2)

  def draw_piece(self, piece: str, startx: int, starty: int) -> None:
    ''' lookup dictionary function to draw a piece based on its name '''
    piece_functions = {
      "lpss": self.draw_large_purple_solid_square,
      "spss": self.draw_small_purple_solid_square,
      "lphs": self.draw_large_purple_hollow_square,
      "sphc": self.draw_small_purple_hollow_circle,
      "lpsc": self.draw_large_purple_solid_circle,
      "sgsc": self.draw_small_green_solid_circle,
      "spsc": self.draw_small_purple_solid_circle,
      "lghc": self.draw_large_green_hollow_circle,
      "lphc": self.draw_large_purple_hollow_circle,
      "sghc": self.draw_small_green_hollow_circle,
      "sphs": self.draw_small_purple_hollow_square,
      "lgss": self.draw_large_green_solid_square,
      "sgss": self.draw_small_green_solid_square,
      "lghs": self.draw_large_green_hollow_square,
      "sghs": self.draw_small_green_hollow_square,
      "lgsc": self.draw_large_green_solid_circle,
    }
    if piece in piece_functions:
      piece_functions[piece](startx, starty)
    else:
      print(f"Error: Unknown piece name '{piece}'")
   

q = Quarto()
