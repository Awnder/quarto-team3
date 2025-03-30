import tkinter as tk
from PieceDrawer import PieceDrawer

class GameBoard:
    def __init__(self, canvas: tk.Canvas):
        self.canvas = canvas
        self.board = [[None for _ in range(4)] for _ in range(4)]
        
        self.piece_played = {}
        self.selected_piece = None
        self.piece_drawer = PieceDrawer(canvas)

        self.draw_board()
        self.bind_clicks()
        self.bind_highlight()

    def select_piece(self, tag: str) -> bool:
        """Selects a piece if clicked.
        Args:
            tag (str): The tag of the piece to be selected.
        Returns:
            bool: True if the piece was successfully selected, False if already played.
        """
        if self.piece_played[tag]:
            print(f"Piece {tag} has already been played!")
            return False
        else:
            self.selected_piece = tag
            print(f"Piece selected: {self.selected_piece}")
            return True

    def place_piece(self, tag: str) -> bool:
        """Places a selected piece on an empty grid slot.
        Args:
            tag (str): The tag of the grid slot where the piece is to be placed.
        Returns:
            bool: True if the piece was successfully placed, False otherwise.
        """
        if not self.selected_piece:
            print("No piece selected!")
            return False

        # Get the grid slot tag
        _, i, j = tag.split("-")
        i, j = int(i), int(j)

        # Check if the slot is empty
        if self.board[j][i] is not None:
            print(f"Slot ({i}, {j}) is already occupied!")
            return False
        
        # Get grid slot coordinates
        x1, y1, x2, y2 = self.canvas.coords(tag)
        slot_center_x = (x1 + x2) / 2
        slot_center_y = (y1 + y2) / 2

        # Get box of the selected piece
        piece_coords = self.canvas.bbox(self.selected_piece)
        if not piece_coords:
            print("Error: Could not get selected piece coordinates!")
            return False
        
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
        return True

    def draw_board(self) -> None:
        """draws all pieces and board"""
        self.piece_drawer.draw_piece("lpss", 250, 75)
        self.piece_played["lpss"] = False
        self.piece_drawer.draw_piece("lpsc", 250, 305)
        self.piece_played["lpsc"] = False
        self.piece_drawer.draw_piece("spss", 275, 535)
        self.piece_played["spss"] = False
        self.piece_drawer.draw_piece("spsc", 275, 665)
        self.piece_played["spsc"] = False
        self.piece_drawer.draw_piece("lphs", 250, 190)
        self.piece_played["lphs"] = False
        self.piece_drawer.draw_piece("lphc", 250, 420)
        self.piece_played["lphc"] = False
        self.piece_drawer.draw_piece("sphs", 275, 600)
        self.piece_played["sphs"] = False
        self.piece_drawer.draw_piece("sphc", 275, 730)
        self.piece_played["sphc"] = False
        self.piece_drawer.draw_piece("lgss", 50, 75)
        self.piece_played["lgss"] = False
        self.piece_drawer.draw_piece("lgsc", 50, 305)
        self.piece_played["lgsc"] = False
        self.piece_drawer.draw_piece("sgss", 75, 535)
        self.piece_played["sgss"] = False
        self.piece_drawer.draw_piece("sgsc", 75, 665)
        self.piece_played["sgsc"] = False
        self.piece_drawer.draw_piece("lghs", 50, 190)
        self.piece_played["lghs"] = False
        self.piece_drawer.draw_piece("lghc", 50, 420)
        self.piece_played["lghc"] = False
        self.piece_drawer.draw_piece("sghs", 75, 600)
        self.piece_played["sghs"] = False
        self.piece_drawer.draw_piece("sghc", 75, 730)
        self.piece_played["sghc"] = False

        # have to draw 16 rectangles instead of lines in order to highlight them upon mouseover
        for i in range(4):
            for j in range(4):
                # instead of 200, use 202 to create 2px extra space between squares so highlight doesn't overlap
                id = self.canvas.create_rectangle(400 + 200 * i, 50 + 200 * j, 600 + 200 * i, 250 + 200 * j, fill="white", outline="black", width=1)
                self.canvas.addtag_withtag(f"board-{i}-{j}", id)

    def bind_clicks(self):
        """Binds mouse clicks for selecting and placing pieces."""
        for id in self.canvas.find_all():
            tags = self.canvas.gettags(id)
            if tags and not tags[0].startswith("board-") and not tags[0].startswith("category-"):
                # Bind piece selection to the first tag of the piece
                self.canvas.tag_bind(
                    tags[0],
                    "<Button-1>",
                    lambda event, tag=tags[0]: self.select_piece(tag),
                )
            elif tags and tags[0].startswith("board-") and not tags[0].startswith("category-"):
                # Bind grid slot placement
                self.canvas.tag_bind(
                    tags[0],
                    "<Button-1>",
                    lambda event, tag=tags[0]: self.place_piece(tag),
                )

    def bind_highlight(self):
        """Binds mouse events for highlighting grid slots."""
        for id in self.canvas.find_all():
            tags = self.canvas.gettags(id)
            if tags and tags[0].startswith("board-") and not tags[0].startswith("category-"):
                # Bind mouse enter and leave events for highlighting
                self.canvas.tag_bind(
                    tags,
                    "<Enter>",
                    lambda event, tag=tags: self.canvas.itemconfig(tag, fill="lightblue"),
                )
                self.canvas.tag_bind(
                    tags[0],
                    "<Leave>",
                    lambda event, tag=tags: self.canvas.itemconfig(tag, fill="white"),
                )