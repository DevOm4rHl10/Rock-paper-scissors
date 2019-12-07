x = input("What is the number of turns? ")
points = 0
for y in range(0, int(x)):
        player_type = input("rock (r) paper(p) or scissors (s) ")
        computer_type = ("Rock", "paper", "scissors")
        import random
        r = random.randint(0, 2)
        computer_pick = computer_type[r]
        if player_type == "r":
          print("you picked Rock, computer picked ", computer_pick)
          if computer_pick == "paper":
              points = points - 1
              print("You lost, current points are : " + str(points))
          elif computer_pick == "scissors":
              points = points + 1
              print("You won, current points are : " + str(points))
          elif computer_pick == player_type:
              print("It's a draw, current points are : " + str(points))
              
        elif player_type == "s":
                print("you picked scissors, computer picked ", computer_pick)
                if computer_pick == "Rock":
                        points = points - 1
                        print("You lost, current points are : " + str(points))
                elif computer_pick == "paper":
                        points = points + 1
                        print("You won, current points are : " + str(points))
                elif computer_pick == player_type:
                        print("It's a draw, current points are : " + str(points))
        
        elif player_type == "p":
                      print("you picked paper, computer picked ", computer_pick)
                      if computer_pick == "scissors":
                              points = points - 1
                              print("You lost, current points are : " + str(points))
                      elif computer_pick == "Rock":
                              points = points + 1
                              print("You won, current points are : " + str(points))
                      elif computer_pick == player_type:
                              print("It's a draw, current points are : " + str(points))
        y = 0
        y = y + 1
        if y == x:
            break
            
        
                
