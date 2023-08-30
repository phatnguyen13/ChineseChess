import numpy as np
pieces_position = {
    'bxe': 0, 'bma': 1, 'bvo': 2, 'bsi': 3, 'btu': 4,
    'bph': 5, 'bch': 6,
    'rxe': 7, 'rma': 8, 'rvo': 9, 'rsi': 10, 'rtu': 11,
    'rph': 12, 'rch': 13
}
turn_position = {'w': 0, 'b': 1}
def one_hot_encode(board):

  board3d = np.zeros((14,10,9), dtype=np.int8)

  for row in range(10):
    for col in range(9):
      cell = board[row][col]
      if cell == '---': continue

      idx = pieces_position[cell]
      board3d[idx][row][col] = 1

  return board3d