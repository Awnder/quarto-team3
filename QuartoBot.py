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

