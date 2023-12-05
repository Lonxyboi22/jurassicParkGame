import requests
import json
import random

response_API = requests.get('https://dinosaur-facts-api.shultzlab.com/dinosaurs')
dinosaur = response_API.json()

dino_file = 'dinosaurs.txt'
name = ""
rand_item = ["Pistol", "Crowbar", "Shotgun", "Knife", "Machette", "Nothing"]
weapon = False
appeared_dino = ""

def dinosaur_appears():
    print("You hear something nearby in the bushes...")
    with open(dino_file, 'r+') as dinos:
        rand_dino_list = dinos.readlines()
        new_list = []
        userInput = ""
        for word in rand_dino_list:
          word = word.strip('\n')
          new_list.append(word)
        dino_num = random.randint(0, 11)
        appeared_dino = new_list[dino_num]
        print("Suddenly, a " +appeared_dino+ "becomes visable in the brush.")
        if appeared_dino == "Tyrannosaurus Rex" or appeared_dino == "Utahraptor" or appeared_dino == "Therizinosaurus":
          print("Before you can react fast enough, the " +appeared_dino+ "attacks and kills you. You are dead.")
          return False
        elif appeared_dino == "Velociraptor" or appeared_dino == "Spinosaurus" or appeared_dino == "Quetzalcoatlus":
          print("The " +appeared_dino+ "seems to not have noticed you yet.\n Would you like to attack or flee?")
          print("Options: fight/flee")
          userInput = input()
          if userInput == "fight" and weapon == True:
            print("You use your item found earlier to try and fend off the " +appeared_dino+ ".")
            if appeared_dino == "Velociraptor":
              print("Since " +appeared_dino+ "is so small, you fend it off!")
              print("You continue on your walk for about a mile.\n You filally find the people you came to the island with!\n They are working on meeting a helicopter in the next few minutes.")
              print("Congrats! You made it!")
              print("Thanks for playing!")
              return False
            else:
              print("Sadly this dino is far too big for you to handle...The " +appeared_dino+ "scoops you up and rips you into shreads.\n You are dead.")
              return False
        elif appeared_dino == "Diloposaurus":
          print("A " +appeared_dino+ "has appeared from the bushes.")
          
        else:
            print("A " +appeared_dino+ "has come out of the tree line. Lucky for you it's an herbavor!")
            print("You silently sneak farther down the path away from the " + appeared_dino)
            print("You continue on your walk for about a mile.\n You filally find the people you came to the island with!\n They are working on meeting a helicopter in the next few minutes.")
            print("Congrats! You made it!")
            print("Thanks for playing!")
            return False

def building_yes():
  lockerOptions = ""
  print("You find a window near the base of the building that seems like you would fit through.")
  print("Searching around you find a decent sized rock and smash the window.")
  print("You knock the remaining glass inward and shimmy through the now open window.")
  print("Looking around, you notice you are now in a small room with a couple lockers.\n Do you want to open a locker?")
  print("Options: yes/no")
  if lockerOptions == "yes":
    lockerNum = random.randint(1, 5)
    itemNum = random.randint(0, 5)
    print("You open locker number", lockerNum)
    print("Inside the locker you found "+rand_item[itemNum])
    if rand_item == "Nothing":
      weapon = False
    else:
      weapon = True
    print("After searching a locker you try the door leading to the rest of the building.")
    print("The door is locked.")
    print("Since you cannot explore the rest of the building you leave through the window and continue down the path.")
    return "no"
    

def game_start():
  directions = ["path 1", "path 2", "path 3", "back to the jungle"]
  print("You are currently walking through the jungle. Suddenly you come to a dirt road that forks into three paths. Where would you like to go?")
  userInput = ""
  userInput2 = ""
  while userInput not in directions:
    print("Options: path 1/path 2/path 3/back to the jungle")
    userInput = input()
    if userInput == "path 1":
      print("You take a left down to the first path you see.\n The jungle thickens as you are walking down the path.\n After about ten minutes of walking, the jungle seems to engold you and the sky begins to get dark.\n")
      dinosaur_appears()
    elif userInput == "path 2":
      print("You take the middle path.\n As you travel down this path, you see a building in the distance.\n")
      print("As you get closer, the building looms overhead.")
      print("Would you like to enter the building?")
      print("Options: yes/no")
      userInput2 = input()
      if userInput2 == "yes":
        building_yes()
      else:
        print("You continue down the path for about another 10 minutes past the building.\n ")
        dinosaur_appears()
    elif userInput == "path 3":
      userInput3 = ""
      print("You continue down the last path for about 15 minutes.")
      print("As you walk down the road, you come upon a slow moving river at the end of the path.\n You notice the path continue on the other side of the river.\n Do you want to try and cross the river or turn back?")
      print("Options: cross/turn back")
      userInput3 = input()
      if userInput3 == "cross":
        print("You slowly wade into the water, watching the river flow around you.")
        print("Rapidly, the pebbled gorund gives away under your feet, forcing you to swim the rest of the way.")
        print("Suddenly, a dark mass from the depths of the river speeds by near you.")
        print("Cautiously, you swim you start swimming a bit faster.")
        print("You estimate you are about a minute from where your feet can touch the ground when all of a sudden something grabs you by the leg and pulls you under the surface.")
        print("You start to panic and try the struggle but the pain of whatever got you was too much.")
        print("You suddenly need to breathe and can't get away.\n You have accepted drowning to be your fate.\n Slowly, your vision slips into black.\n You died by drowning..")
        return False
      else:
        print("You turn back and end up back at the 3 paths.")
        userInput = "dinos"
        return userInput

    elif userInput == "back to the jungle":
      print("As you begin to turn around, a loud booming noise quickly approaching can be heard close by.")
      print("You start to book it down a random path but to no avail, a Tyrannosaurus Rex has appeared from the tree line cutting you off mid sprint.")
      print("The T-Rex swiftly picks you up with its sharp teeth sinking into your abdomin.\n In excrutiating pain, you try to struggle away but begin to feel weak from blood loss.")
      print("The T-Rex clamps down, biting you clean in half.\n You died from blood loss.")
    else: 
      print("Please enter a valid option.")



def intro():
  options = ["continue", "quit"]
  print("Would you like to continue on with the adventure?")
  userInput = ""
  while userInput not in options:
    print("Options: continue/quit")
    userInput = input()
    if userInput == "continue":
      game_start()
    elif userInput == "quit":
      return False
    else:
      print("Please enter a valid option!")
      



if __name__ == "__main__":
    while True:
      print("Welcome, to Jurassic Park (Game)!")
      print("Let's start with your name: ")
      name = input()
      print("As a world renound paleontologist, you have been invited to Jurassic Park.")
      print("However, while visiting the park, the dinosaurs have gotten loose thanks to that loser Nedry.")
      print("You also have been separated from the rest of the group, what will you do " +name+ "?")
      
      intro()
      