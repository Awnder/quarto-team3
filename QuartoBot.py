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
        """ Selects the first piece that is not placed on the board """
        pieces_remaining = [piece for piece in pieces if not pieces[piece]]
        piece = pieces_remaining[0]
        print(f'Bot selected piece: {piece}')
        return piece

    def place_piece(self, board: list[list[bool]], pieces: dict[str, bool], piece: str) -> tuple[list[list[bool]], dict[str, bool]]:
        """ Places the piece at the first empty position """
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                if not cell:
                    board[i][j] = True
                    pieces[piece] = True
                    print(f'Bot placed piece: {piece} at ({i}, {j})')
                    return board, pieces

        print("Bot unable to place piece")    
        return board, pieces