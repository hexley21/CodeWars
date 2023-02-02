def valid_solution(board):
    rows = [set(x) for x in board]
    columns = [set([j[i] for j in board]) for i in range(len(board))]
    blocks = [[], [], [], [], [], [], [], [], []]
    x = 0
    z = 0
    for i in range(9):
        for j in range(z, 3 + z):
            for k in range(x, 3 + x):
                blocks[i].append(board[j][k])
        x += 3
        if (x == 9):
            x = 0
            z += 3

    # Validates rows, columns and blocks
    for i in range(9):
        if {1, 2, 3, 4, 5, 6, 7, 8, 9} != rows[i]:
            print(f"#{i} row is invalid")
            return False
        if {1, 2, 3, 4, 5, 6, 7, 8, 9} != columns[i]:
            print(f"#{i} column is invalid")
            return False
        if {1, 2, 3, 4, 5, 6, 7, 8, 9} != set(blocks[i]):
            print(f"#{i} block is invalid")
            return False
    return True
