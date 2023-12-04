import requests
import json
import random
import dinosaurs.txt

response_API = requests.get('https://dinosaur-facts-api.shultzlab.com/dinosaurs')
dinosaur = response_API.json()

dino_file = dinosaurs.txt
name = ""
weapon = False

with open(dino_file, 'r+') as dinos:
  def dinosaur_appears():
     
    print("You hear something nearby in the bushes...")



  def game_start():
    directions = ["path 1", "path 2", "path 3", "back to the jungle"]
    print("You are currently walking through the jungle. Suddenly you come to a dirt road that forks into three paths. Where would you like to go?")
    userInput = ""
    while userInput not in directions:
      print("Options: path 1/path 2/path 3/back to the jungle")
      userInput = input()
      if userInput == "path 1":
        print("You take a left down to the first path you see. The jungle thickens as you are walking down the path.\n After about ten minutes of walking, the jungle seems to engold you and the sky begins to get dark.\n")
        dinosaur_appears()
      elif userInput == "path 2":
        print("wow")
      elif userInput == "path 3":
        print("hey!")
      elif userInput == "back to the jungle":
        print("Thicc")
      else: 
        print("Please enter a valid option.")



    def intro():
      options = ["continue", "quit"]
      print("Would you like to continue?")
      userInput = ""
      while userInput not in options:
        print("Options: continue/quit")
        userInput = input()
        if userInput == "continue":
          game_start()
        elif userInput == "quit":
          quit()
        else:
          print("Please enter a valid option!")
      



    if __name__ == "__main__":
        while True:
          print("Welcome, to Jurassic Park (Game)!")
          print("Let's start with your name: ")
          name = input()
          print("As a world renound paleontologist, you have been invited to Jurassic Park.")
          print("However, while visiting the park, the dinosaurs have gotten loose thanks to that loser Nedry.")
          print("You also have been separated from the rest of the group, what will you do" +name+ "?")
        
          intro()