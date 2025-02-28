import numpy as np

array_zeros = np.zeros((2, 2), dtype=int)
array_zeros[np.random.randint(0, 2), np.random.randint(0, 2)] = 1

moves_counter = 0

while True:
    user_move = input("Digite a posição que deseja conferir (linha coluna): ")
    user_move = user_move.split(" ")

    if array_zeros[int(user_move[0]), int(user_move[1])] == 1:
        print("Game over, try again!")
        break
    moves_counter += 1
    if moves_counter == 3:
        print("Congratulations! You beat the game! :)")
        break

