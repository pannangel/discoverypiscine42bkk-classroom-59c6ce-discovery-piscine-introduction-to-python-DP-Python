#!/usr/bin/env python3
def chessboard(board_grid): #creat chess board
    board = []
    for row in board_grid.strip().split('\n'):
        clean = row.strip()
        if clean:
            board.append(list(clean))

    board_size = len(board) #check if it's square
    for row in board:
        if len(row) != board_size:
            print("Fail")
            return

    king = None #find the king locate
    for x in range(board_size): #x represent the row
        for y in range(board_size): #y represent the column
            if board[x][y] == 'K':
                if king is None:
                    king = (x, y) #save the king locate
                else:
                    print("Fail") #if more than one king it's fail
                    return
    if not king: #no king it's fail
        print("Fail")
        return

    king_row, king_col = king

    Directions = {
        'R': [(-1, 0), (1, 0), (0, -1), (0, 1)],
        'B': [(-1, -1), (-1, 1), (1, -1), (1, 1)],
        'Q': [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)],
        'P': [(1, -1), (1, 1)]
    }

    for piece, dirs in Directions.items():                      #Checking the direction from the king position according to specific pieces
        for dx, dy in dirs:                                     # For each piece, loop through its directions(dx,dy)
            x, y = king_row + dx, king_col + dy                 # Move one step away from the king position

            if piece == 'P':                                    # Checking the Pawns
                if 0 <= x < board_size and 0 <= y < board_size: # If it is within in bounds, check if there is a piece
                    if board[x][y] == 'P':                      # "Pawn" Found, then the king is in check
                        print("Success")
                        return
                continue

            while 0 <= x < board_size and 0 <= y < board_size:  # while it is within in bounds, check the threats
                if board[x][y] == '.':                          # "Empty" Found, keep continue checking 
                    x += dx                                     # The king position will be added up based on the specific moves of pieces
                    y += dy
                elif board[x][y] == piece:                      # Found "piece", the king is in check
                    print("Success")
                    return
                else:
                    break                                       # If any pieces blocking, break the loop

    print("Fail")     