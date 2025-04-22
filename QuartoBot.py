class QuartoBot:
    def __init__(self):
        pass

    def select_piece(self, board: list[list[bool]], pieces: dict[str, bool]) -> str:
        """ Implement this method to select a piece to give to the opponent """
        pass

    def place_piece(self, board: list[list[bool]], pieces: dict[str, bool]):
        """ Implement this method to place a piece on the board """
        pass

class QuartoTestBot(QuartoBot):
    def __init__(self):
        pass
        
    def select_piece(self, board: list[list[bool]], pieces: dict[str, bool]) -> str:
        """Selects the first piece that is not placed on the board 
        Args:
            board (list[list[bool]]): The current state of the board
            pieces (dict[str, bool]): The current state of the pieces
        Returns:
            str: The piece to be selected
        """
        pieces_remaining = [piece for piece in pieces if not pieces[piece]]
        piece = pieces_remaining[0]
        print(f'Bot selected piece: {piece}')
        return piece

    def place_piece(self, board: list[list[str]], pieces: dict[str, bool], piece: str) -> tuple[int, int]:
        """Effectively places the piece at the first empty position by returning the position of the desired board location
        Use the Quarto.place_piece method to handle the piece placing logistics like tag manipulation and board state

        Args:
            board (list[list[str]]): The current state of the board
            pieces (dict[str, bool]): The current state of the pieces
            piece (str): The piece to be placed 
        Returns:
            tuple (int, int): The position where the bot wants to place the piece
        """
        for i, row in enumerate(board):
            for j, tag in enumerate(row):
                if tag is None:  # Look for an empty slot
                    print(f'Bot placed piece: {piece} at position ({i}, {j})')
                    return j, i

        print("Bot unable to place piece")    
        return -1, -1

class SmarterQuartoBot(QuartoBot):
    def __init__(self):
        super().__init__()

    def select_piece(self, board: list[list[str]], pieces: dict[str, bool]) -> str:
        """
        Picks first available piece
        """
        pieces_remaining = [p for p, used in pieces.items() if not used]
        for piece in pieces_remaining:
            # Naively assume this piece won't let the opponent win.
            return piece
        return None

    def place_piece(self, board: list[list[str]], pieces: dict[str, bool], piece: str) -> tuple[int, int]:
        """
        Try placing the piece in a spot that gives us a potential win,
        otherwise fall back to the first open spot
        """
        # First: look for a row/col/diag with 3 matching characteristics
        def get_tag(x, y):
            return board[y][x] if board[y][x] else None

        # Try to complete a line
        for y in range(4):
            row = [get_tag(x, y) for x in range(4)]
            if row.count(None) == 1:
                x = row.index(None)
                return x, y

        for x in range(4):
            col = [get_tag(x, y) for y in range(4)]
            if col.count(None) == 1:
                y = col.index(None)
                return x, y

        main_diag = [get_tag(i, i) for i in range(4)]
        if main_diag.count(None) == 1:
            idx = main_diag.index(None)
            return idx, idx

        anti_diag = [get_tag(3 - i, i) for i in range(4)]
        if anti_diag.count(None) == 1:
            idx = anti_diag.index(None)
            return 3 - idx, idx

        # Fallback: first open slot
        for y in range(4):
            for x in range(4):
                if board[y][x] is None:
                    return x, y

        return -1, -1
