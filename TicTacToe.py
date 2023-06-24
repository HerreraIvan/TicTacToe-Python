import msvcrt
sym_board = {2: "-", 3: "X", 5: "O", }  # imprime los simbolos
X = 3
O = 5
blankSpace = 2
turnCont = 1
board = [[blankSpace]*3 for _ in range(3)]  # genera el tablero

def procesar_posicion(posicion):
    fila, columna = posicion.split(",")
    return [int(fila)-1, int(columna)-1]

def posicion_correcta(posicion):
    if 0 <= posicion[0] <= 2 and 0 <= posicion[1] <= 2:
        if board[posicion[0]][posicion[1]] == blankSpace:
            return True
    return False

def mostrar_board():
    print("")
    for fila in board:
        for col in fila:
            print(sym_board[col], end=' ')
        print('')

def empate():
    for f in board:
        for c in f:
            if c == blankSpace:
                return False
    return True

def actualizar_board(posicion, X):
    board[posicion[0]][posicion[1]] = X
    return board

def Make2(board, O):
    if board[1][1] == 2:  # Verifica que la casilla del centro esta ocupada
        board[1][1] = O
        return 4
    if (Posswin(board, O) == -1):
        if board[0][0] == 2:
            board[0][0] = O
        elif board[0][2] == 2:
            board[0][2] = O
        elif board[2][0] == 2:
            board[2][0] = O
        elif board[2][2] == 2:
            board[2][2] = O

    return False


def siGana(board):
    # ---------------------VERFICA SI O GANA en filas --------------------
    if board[0][0] * board[0][1] * board[0][2] == 125 or board[1][0] * board[1][1] * board[1][2] == 125 or board[2][0] * board[2][1] * board[2][2] == 125:
        return True
    if board[0][0] * board[0][1] * board[0][2] == 27 or board[1][0] * board[1][1] * board[1][2] == 27 or board[2][0] * board[2][1] * board[2][2] == 27:
        return True
    # ---------------------VERFICA SI O GANA en columnas--------------------
    if board[0][0] * board[1][0] * board[2][0] == 125 or board[0][1] * board[1][1] * board[2][1] == 125 or board[0][2] * board[1][2] * board[2][2] == 125:
        return True
    if board[0][0] * board[1][0] * board[2][0] == 27 or board[0][1] * board[1][1] * board[2][1] == 27 or board[0][2] * board[1][2] * board[2][2] == 27:
        return True
    # ---------------------si gana DIAGONAL--------
    if board[0][0] * board[1][1] * board[2][2] == 125:
        return True
    if board[0][0] * board[1][1] * board[2][2] == 27:
        return True
        # ---------------------si gana DIAGONAL inversa--------
    if board[0][2] * board[1][1] * board[2][0] == 125:
        return True
    if board[0][2] * board[1][1] * board[2][0] == 27:
        return True

def Posswin(board, O):
     # ---------------------FILAS GANA--------------------------------------
    if board[0][0] * board[0][1] * board[0][2] == 50:
        if board[0][2] == 2:
            board[0][2] = O
            return True
        elif board[0][0] == 2:
            board[0][0] = O
            return True
        elif board[0][1] == 2:
            board[0][1] = O
            return True

    elif board[1][0] * board[1][1] * board[1][2] == 50:
        if board[1][2] == 2:
            board[1][2] = O
            return True
        elif board[1][0] == 2:
            board[1][0] = O
            return True
        elif board[1][1] == 2:
            board[1][1] = O
            return True
    elif board[2][0] * board[2][1] * board[2][2] == 50:
        if board[2][2] == 2:
            board[2][2] = O
            return True
        elif board[2][0] == 2:
            board[2][0] = O
            return True
        elif board[2][1] == 2:
            board[2][1] = O
            return True

# ---------------------COLUMNAS--------------------------------------
    if board[0][0] * board[1][0] * board[2][0] == 50:
        if board[2][0] == 2:
            board[2][0] = O
            return True
        elif board[0][0] == 2:
            board[0][0] = O
            return True
        elif board[1][0] == 2:
            board[1][0] = O
            return True
    elif board[0][1] * board[1][1] * board[2][1] == 50:
        if board[2][1] == 2:
            board[2][1] = O
            return True
        elif board[0][1] == 2:
            board[0][1] = O
            return True
        elif board[1][1] == 2:
            board[1][1] = O
            return True
    elif board[0][2] * board[1][2] * board[2][2] == 50:
        if board[2][2] == 2:
            board[2][2] = O
            return True
        elif board[0][2] == 2:
            board[0][2] = O
            return True
        elif board[1][2] == 2:
            board[1][2] = O
            return True

# ---------------------DIAGONAL--------------------------------------
    if board[0][0] * board[1][1] * board[2][2] == 50:
        if board[2][2] == 2:
            board[2][2] = O
            return True
        elif board[0][0] == 2:
            board[0][0] = O
            return True
        elif board[1][1] == 2:
            board[1][1] = O
            return True

# ---------------------DIAGONAL INVERSA---------------------------------
    if board[0][2] * board[1][1] * board[2][0] == 50:
        if board[0][2] == 2:
            board[0][2] = O
            return True
        elif board[2][0] == 2:
            board[2][0] = O
            return True
        elif board[1][1] == 2:
            board[1][1] = O
            return True  
# ---------------------FILAS TAPA--------------------------------------
    if board[0][0] * board[0][1] * board[0][2] == 18:
        if board[0][2] == 2:
            board[0][2] = O
        elif board[0][0] == 2:
            board[0][0] = O
        elif board[0][1] == 2:
            board[0][1] = O
        return True
                   
    elif board[1][0] * board[1][1] * board[1][2] == 18:
        if board[1][2] == 2:
            board[1][2] = O
            return True
        elif board[1][0] == 2:
            board[1][0] = O
            return True
        elif board[1][1] == 2:
            board[1][1] = O
            return True
    elif board[2][0] * board[2][1] * board[2][2] == 18:
        if board[2][2] == 2:
            board[2][2] = O
            return True
        elif board[2][0] == 2:
            board[2][0] = O
            return True
        elif board[2][1] == 2:
            board[2][1] = O
            return True
  # ---------------------COLUMNAS--------------------------------------        
    if board[0][0] * board[1][0] * board[2][0] == 18:
        if board[2][0] == 2:
            board[2][0] = O
            return True
        elif board[0][0] == 2:
            board[0][0] = O
            return True
        elif board[1][0] == 2:
            board[1][0] = O
            return True
    elif board[0][1] * board[1][1] * board[2][1] == 18:
        if board[2][1] == 2:
            board[2][1] = O
            return True
        elif board[0][1] == 2:
            board[0][1] = O
            return True
        elif board[1][1] == 2:
            board[1][1] = O
            return True
    elif board[0][2] * board[1][2] * board[2][2] == 18:
        if board[2][2] == 2:
            board[2][2] = O
            return True
        elif board[0][2] == 2:
            board[0][2] = O
            return True
        elif board[1][2] == 2:
            board[1][2] = O
            return True

# ---------------------DIAGONAL--------------------------------------   
    if board[0][0] * board[1][1] * board[2][2] == 18:
        if board[2][2] == 2:
            board[2][2] = O
            return True
        elif board[0][0] == 2:
            board[0][0] = O
            return True
        elif board[1][1] == 2:
            board[1][1] = O 
            return True
    if board[0][0] * board[1][1] * board[2][2] == 125:
        return True
    if board[0][0] * board[1][1] * board[2][2] == 27:
        return True
# ---------------------DIAGONAL INVERSA---------------------------------
    if board[0][2] * board[1][1] * board[2][0] == 18:
        if board[0][2] == 2:
            board[0][2] = O
            return True
        elif board[2][0] == 2:
            board[2][0] = O
            return True
        elif board[1][1] == 2:
            board[1][1] = O  
            return True
    if  board[0][2] * board[1][1] * board[2][0] == 125:
        return True
    if  board[0][2] * board[1][1] * board[2][0] == 27:
        return True
   
    return -1


def go(turnCont):
    if turnCont in [1, 3, 5, 7, 9]:
        return 3
    if turnCont in [2, 4, 6, 8]:
        return 5

def juego():
    global turnCont
    mostrar_board()
    turnCont = 1
    while True:
        if go(turnCont) == 3:
            posicion = input(
                "Juega humano, elige una posicion de 1 a 3 separada por , (fila, columna) ")
        try:
            posicion_l = procesar_posicion(posicion)
        except:
            print("Error, la posicion no es valida, ingresa una posicion correcta separada por coma (fila,columna) ")
            continue

        if posicion_correcta(posicion_l):
            actualizar_board(posicion_l, X)
            print("Tiro del humano: ")
            mostrar_board()
            turnCont = turnCont + 1
        else:
            print("Ingresa una posicion correcta 1 a 3 (fila,columna). ")
        if go(turnCont) == 5:
            turnCont = turnCont + 1
            if((Posswin(board, O) == -1)):
                Make2(board, O)
                actualizar_board(posicion_l, X)
                #mostrar_board()
            print("Tiro de la computadora: ")
            mostrar_board()

        if siGana(board):
            mostrar_board()
            print("CPU ha ganado!!!")
            msvcrt.getch()
            break
        if empate():
            mostrar_board()
            print("Es un empate")
            msvcrt.getch()
            break
juego()
