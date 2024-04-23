print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
print("You are at a crossroad. Where do you want to go?\n")
choice1=input("Type 'L' for left and 'R' for right\n").lower()
if choice1=='l' :
  print("You have reached a lake. There is an island in the middle  of the lake.\n")
  choice2=input("Type 'S' to swim and 'W' to wait\n")
  if choice2=='W':
    print("Theres a boat coming. You have reached the island safely.\n There's a house with 3 doors.\nThe red one, yellow and the otherone is blue, which door do you choose??")
    choice3=input("Enter 'R' for red, 'Y' for yellow and 'B' for blue\n")
    if choice3=='Y':
      print("You win!, Congratulations you have found the treasure\n")
    elif choice3=='R':
      print("Burned by fire. Game over.\n")
    elif choice3=='B':
      print("Eaten by Beasts. Game over.\n")
    else:
      print("Game over.\n")
  else:
    print("Attacked by trout. Game over.\n")

else:
  print("Fall into a hole. Game over.\n")

