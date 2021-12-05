from numpy import array

with open('inputs/day4_draw.txt') as file:
    txt = file.read()
    draws = tuple(map(int, txt.split(sep=',')))

with open('inputs/day4_cards.txt') as file:
    txt = file.read()
    cards = tuple(map(str, txt.split(sep='\n\n')))


class BingoCard:
    def __init__(self, card_data: str):
        self._data = [
            [int(item) for item in row.split(' ') if item != '']
            for row in card_data.split('\n')
        ]

        self._card_status = array([[False for _ in row] for row in self._data])

        self.card = [
            [int(item) for item in row.split(' ') if item != '']
            for row in card_data.split('\n')
        ]

    def __str__(self):
        return '\n'.join(
            [
                ', '.join([f"{item:>2}" for item in row])
                for row in self.card
            ]
        )

    def __repr__(self):
        return self.__str__()

    def update(self, number: int):
        row, col = self._find_index(number)

        if (row is not None) and (col is not None):
            self.card[row][col] = 'X'
            self._card_status[row][col] = True
        else:
            return

    def _update_card_status(self, row_pos, col_pos):
        self._card_status[row_pos][col_pos] = True

    def _find_index(self, target):
        for idx_r, row in enumerate(self.card):
            if target in row:
                for idx_c, item in enumerate(row):
                    if item == target:
                        return idx_r, idx_c
        return None, None

    def check_bingo(self):
        for idx, row in enumerate(self._card_status):
            if False not in set(row):
                return idx, True

        for idx, row in enumerate(self._card_status.T):
            if False not in set(row):
                return idx, True

        return -1, False


if __name__ == '__main__':

    BingoCards: list = [
        BingoCard(i) for i in cards
    ]

    for draw in draws:

        for idx, card in enumerate(BingoCards):
            bingo = False

            if card is not None:
                card.update(draw)
                row, bingo = card.check_bingo()

            if bingo:
                winner = BingoCards[idx]

                flattened = [
                    [item for item in row if str(item).isdigit()]
                    for row in winner.card
                ]

                total = list(map(sum, flattened))
                print(f"{sum(total)=}, {draw=},{sum(total) * draw = }")

                BingoCards[idx] = None
