import random
list=['s','w','g']
print("\t\t\t Snake, Water ,Gun Game")
print("s for Snake\nw for Water\ng for Gun")
chance = 10
H_points=0
c_points=0
no_of_chance=0

while no_of_chance< chance:
    inp=input('Snake,Water,Gun:')
    rand = random.choice(list)

    if inp== random:
        print("tie Both 0 point to each \n")
# if user enter

    if inp =="s" and rand=="g":

        c_points += 1
        print(f"computer guess :{rand} and human guess:{inp}")
        print(f"Score: computer :{c_points} \t human:{H_points}\n")

    elif   inp == "s" and rand == "w":
      H_points += 1
      print(f"computer guess :{rand} and human guess:{inp}")
      print(f"Score: computer :{c_points} \t human:{H_points}\n")

    elif inp =="w" and rand=="g" :
      H_points += 1
      print(f"computer guess :{rand} and human guess:{inp}")
      print(f"Score: computer :{c_points} \t human:{H_points}\n")

    elif inp =="w" and rand=="s" :
      c_points += 1
      print(f"computer guess :{rand} and human guess:{inp}")
      print(f"Score: computer :{c_points} \t human:{H_points}\n")

    elif inp =="g" and rand=="s" :
      H_points += 1
      print(f"computer guess :{rand} and human guess:{inp}")
      print(f"Score: computer :{c_points} \t human:{H_points}\n")

    elif inp =="g" and rand=="w" :
      c_points += 1
      print(f"computer guess :{rand} and human guess:{inp}")
      print(f"Score: computer :{c_points} \t human:{H_points}\n")

    else:
        print("wrong input")

    no_of_chance += 1
    print(f"{chance- no_of_chance} is left out of {chance}")
print("GAME OVER")


if(c_points > H_points):
    print("Computer Wins")
else:
    print("Human Wins")

print(f"Computer Score: {c_points} \t Human Score: {H_points}")
