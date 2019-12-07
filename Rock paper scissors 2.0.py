from random import randint
user_points = 0
computer_points = 0
arr = ("rock", "paper", "scissors")
p = "paper"
r = "rock"
s = "scissors"
y = 0
x = int(input("What is the number of turns ? "))
def get_user_move():
    user_move = input("rock(r), paper(p), scissors(s) ")
    if user_move == "r":
        return "rock"
    elif user_move == "p":
        return "paper"
    elif user_move == "s":
        return "scissors"
    else:
        print("unkown move")
        exit(1)


def get_computer_move():
    index = randint(0,2)
    computer_move = arr[index]

    return computer_move

for x in range(0, x):

    user_move = get_user_move() # paper, rock or scissors
    computer_move = get_computer_move()

    moves = [(r, s), (p, r), (s, p)]

    print("You picked", user_move, "computer picked", computer_move)

    if user_move == computer_move:
        print("It's a draw")
    elif (computer_move, user_move) in moves:
        computer_points = computer_points + 1
        print("You lost")
    else:
        user_points = user_points + 1
        print("You won")

    print("current point are : ", user_points, "computer points are : " ,computer_points)
    y = y + 1
    if y == x:
        break
