def accept(n):
    puz = []
    for i in range(n):
        puz.append([val for val in input().split()])
    return puz


def print_board(board, n):
    for i in range(n):
        print()
        for j in range(n):
            print(board[i][j], end=' ')


def find_space(Current, n):
    for blank_row_pos in range(n):
        for blank_col_pos in range(n):
            if Current[blank_row_pos][blank_col_pos] == '_':
                return blank_row_pos, blank_col_pos


def copy_current(Current):
    temp = []
    for i in range(len(Current)):
        row = []
        for val in Current[i]:
            row.append(val)

        temp.append(row)

    return (temp)


def shuffle(Current, brow_pos, bcol_pos, move_x, move_y):
    if move_x >= 0 and move_x < len(Current) and move_y >= 0 and move_y < len(Current):
        temp = []
        temp = copy_current(Current)
        change = temp[move_x][move_y]
        temp[move_x][move_y] = temp[brow_pos][bcol_pos]
        temp[brow_pos][bcol_pos] = change
        return temp
    else:
        return None


def g_score(Node):
    return Node[1]


def h_score(Current, Goal, n):
    hscore = 0
    for i in range(n):
        for j in range(n):
            if (Current[i][j] != Goal[i][j]) and (Current[i][j] != '_'):
                hscore += 1

    return hscore


def f_score(Node, Goal, n):
    Current = Node[0]
    return g_score(Node) + h_score(Current, Goal, n)


def move_gen(Node, Goal, n):
    Current = Node[0]
    level = Node[1]
    fscore = 0
    row, col = find_space(Current, n)
    move_positions = [[row, col - 1], [row, col + 1],
                      [row - 1, col], [row + 1, col]]

    children = []
    for move in move_positions:
        child = shuffle(Current, row, col, move[0], move[1])
        if child is not None:
            cNode = [child, 0, 0]
            fscore = f_score(cNode, Goal, n)

            Node = [child, level + 1, fscore]
            children.append(Node)
    print("\n\n The Children ::", children)
    return children


def goal_test(Current, Goal, n):
    if h_score(Current, Goal, n) == 0:
        return True
    else:
        return False


def sort(L):
    L.sort(key=lambda x: x[2], reverse=False)
    return L


def play_game(Start, Goal, n):
    fscore = 0
    gscore = 0
    level = 0
    Node = [Start, level, fscore]
    fscore = f_score(Node, Goal, n)

    Node = [Start, level, fscore]
    print("\nThe Node is=\n", Node)
    OPEN = []
    CLOSED = []
    OPEN.append(Node)
    levelcount = 0
    previous = OPEN[0][0]

    while True:

        N = OPEN[0]
        del OPEN[0]

        Current = N[0]
        print("----------->", N)
        print("\n\n The current configuration is ::", Current)

        CLOSED.append(N)
        if goal_test(Current, Goal, n) == True:
            print("\nGoal reached!!")
            print("CLOSED=", CLOSED)
            break

        CHILD = move_gen(N, Goal, n)
        OPEN = []
        for child in CHILD:
            if (child[0] != previous):
                print("Appending --------> " + str(child[0]))
                OPEN.append(child)
        sort(OPEN)
        previous = Current


n = int(input("Enter the board size:"))

print("\nEnter Start Configuration of board")
Start = accept(n)

print("\nEnter Goal Configuration of board")
Goal = accept(n)

play_game(Start, Goal, n)
