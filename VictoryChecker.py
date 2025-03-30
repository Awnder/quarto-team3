import tkinter as tk

class VictoryChecker:
    def __init__(self, board: list[list[bool]], canvas: object):
        self.board = board
        self.canvas = canvas

    def claim_victory(self, claim_direction_entry: tk.StringVar, claim_location_entry: tk.StringVar, claim_characteristic_entry: tk.StringVar) -> bool:
        """
        Claims victory and highlights the winning pieces.

        This method checks if there is a winning condition based on the claim type, location, and characteristic provided.
        If a winning condition is met, it announces the winner and highlights the winning pieces.

        Args:
            claim_direction_entry (tk.StringVar): The type of claim ("row", "column", or "diagonal").
            claim_location_entry (tk.StringVar): The location of the claim (row number, column number, or diagonal type).
            claim_characteristic_entry (tk.StringVar): The characteristic of the claim ("size", "color", "fill", or "shape").
        Returns:
            bool: True if a winning condition is met, False otherwise.
        """
        is_win = None
        claim_type = claim_direction_entry.get()
        claim_location = claim_location_entry.get()
        claim_characteristic = claim_characteristic_entry.get()
        if claim_type == "diagonal":
            is_win = self._check_win_diagonal(claim_location, claim_characteristic)
        else:
            if claim_type == "row":
                is_win = self._check_win_row(int(claim_location) - 1, claim_characteristic)
            elif claim_type == "column":
                is_win = self._check_win_row(int(claim_location) - 1, claim_characteristic)

        return is_win

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

                print(f"check win {tag} at ({row},{col}) count_size: {total_scores[0]}, count_color: {total_scores[1]}, count_fill: {total_scores[2]}, count_shape: {total_scores[3]}")

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

                print(f"check win {tag} at ({row},{col}) count_size: {total_scores[0]}, count_color: {total_scores[1]}, count_fill: {total_scores[2]}, count_shape: {total_scores[3]}")

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

                    print(f"check win {tag} at ({row},{col}) count_size: {total_scores[0]}, count_color: {total_scores[1]}, count_fill: {total_scores[2]}, count_shape: {total_scores[3]}")

            if (total_scores[0] == 4 and characteristic == "size") or (total_scores[1] == 4 and characteristic == "color") or (total_scores[2] == 4 and characteristic == "fill") or (total_scores[3] == 4 and characteristic == "shape"):
                return True
        if diagonal == "anti":
            for row, col in anti:
                if self.board[row][col] is None:
                    continue
                else:
                    tag = self.canvas.gettags(self.board[row][col])[0]

                    total_scores, current_categories = self._check_win_tag_identifier(total_scores, current_categories, tag)

                    print(f"check win {tag} at ({row},{col}) count_size: {total_scores[0]}, count_color: {total_scores[1]}, count_fill: {total_scores[2]}, count_shape: {total_scores[3]}")

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

    def _check_win_any(self) -> bool:
        """
        Checks if a player has won in any row, column, or diagonal.
        Returns True if any winning condition is met.
        """
        characteristic = ["size", "color", "fill", "shape"]
        for c in characteristic:
            for row in range(4):
                if self._check_win_row(row, c):
                    return True

            for col in range(4):
                if self._check_win_col(col, c):
                    return True

            if self._check_win_diagonal("main", c) or self._check_win_diagonal("anti", c):
                return True

        return False