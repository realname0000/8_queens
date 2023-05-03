#!/usr/bin/python3

# find all placements of 8 (or something) queens
board = 8 # 8 is standard size

def attack(q):
    lq = len(q)
    for i in range(lq-1):
            if q[-1] == q[i]:
                return True
            x = lq - 1
            if abs(q[-1]-q[i]) == abs(x - i):
                return True
    return False

def advance():  ## advance and backtrack
    try:
        old = queens.pop()
    except:
        exit(0)
    old += 1
    if old >= board:
        advance()
        return False
    queens.append(old)
    return True

if __name__ == "__main__":
    queens = [0]

    while True:
        while(len(queens) < board):
             while( attack(queens) ):
                 advance()
             queens.append(0)
        check = attack(queens)
        if (not check) and (len(queens) == board):
            print('solution:', queens)
        advance()
