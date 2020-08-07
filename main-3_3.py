import random
import time
from text import story, title, fight_text, game_over, victory, fatality, loading, ending_story, choose
import sys
from pygame import mixer

mixer.init()
mixer.music.load("mkii.wav")
mixer.music.play()


class Character():
    def __init__(self, name, health, punch_power, kick_power, special_power, special_name, defense):
        self.name = name
        self.health = health
        self.punch_power = punch_power
        self.kick_power = kick_power
        self.special_power = special_power
        self.special_name = special_name
        self.defense = defense

    def __str__(self):
        return """
        Name: %s
        Health: %s
        Punch Power: %s
        Kick Power: %s
        Special Power: %s (%d)
        Defense: %s
        """ % (self.name, self.health, self.punch_power, self.kick_power, self.special_name, self.special_power, self.defense)

    def kick(self, opponent):
        if self.kick_power == "low":
            kick = random.randint(1, 3)
        if self.kick_power == "medium":
            kick = random.randint(4, 6)
        if self.kick_power == "high":
            kick = random.randint(7, 9)
        defense = opponent.add_defense()
        if defense > kick:
            defense = kick
        opponent.health -= (kick - defense)
        print("\n\n%s kicked for %d damage to %s." %
              (self.name, kick, opponent.name))
        print("%s blocked with %d defense and has %d health left." %
              (opponent.name, defense, opponent.health))

    def punch(self, opponent):
        if self.punch_power == "low":
            punch = random.randint(1, 3)
        if self.punch_power == "medium":
            punch = random.randint(4, 6)
        if self.punch_power == "high":
            punch = random.randint(7, 9)
        defense = opponent.add_defense()
        if defense > punch:
            defense = punch
        opponent.health -= (punch - defense)
        print("\n\n%s punched for %d damage to %s." %
              (self.name, punch, opponent.name))
        print("%s blocked with %d defense and has %d health left." %
              (opponent.name, defense, opponent.health))

    def special(self, opponent):
        defense = opponent.add_defense()
        if defense > self.special_power:
            defense = self.special_power
        opponent.health -= (self.special_power - defense)
        print("\n\n%s used %s for %d damage to %s." %
              (self.name, self.special_name, self.special_power, opponent.name))
        print("%s blocked with %d defense and has %d health left." %
              (opponent.name, defense, opponent.health))

    def rand_attack(self, opponent):
        random_selection = random.randint(1, 3)
        if random_selection == 1:
            self.punch(opponent)
        if random_selection == 2:
            self.kick(opponent)
        if random_selection == 3:
            self.special(opponent)

    def is_alive(self):
        return self.health > 0

    def add_defense(self):
        if self.defense == "low":
            return random.randint(1, 3)
        if self.defense == "medium":
            return random.randint(4, 6)
        if self.defense == "high":
            return random.randint(7, 9)


# characters
character1 = Character("K. Relly", 50, "high", "high", 30, "Acid Drool", "low")
character2 = Character("Charg'n Ryno", 50, "medium",
                       "low", 30, "Gor'n Horn Of Pain", "medium")
character3 = Character("Cave Dolòn", 50, "high", "low",
                       30, "Nutcracker Choke", "high")
character4 = Character("Snake Jodgel", 50, "high",
                       "medium", 30, "Eye Gouge", "low")
character5 = Character("Ron Sheid", 50, "low", "low", 30, "Bitch Slap", "high")
character6 = Character("Justin", 50, "high", "low",
                       30, "Words Of Fury", "medium")
character7 = Character("NeckBreakin Brit", 50, "low",
                       "high", 30, "Roundhouse Kick To The Face", "high")
character8 = Character("Crazyeyes Chris", 50, "high",
                       "medium", 30, "Stare Of Death", "medium")
character9 = Character("Yelrac Zil", 50, "high", "high",
                       30, "Teleport & Attack From Behind", "low")


# Continue fighting
def keep_playing():
    while len(opponent_list) >= 1:
        keep_playing = input("Do you want to keep fighting? (y or n) ")
        if keep_playing == 'y':
            player.health = 50
            print("\nYou have absorbed power from your opponent!")
            print("You're back to Full Health: %d \n" % (player.health))
            print("Your next opponent is: %s" % (opponent_list[0]))
            fight_text()
            fight()
        elif keep_playing == 'n':
            print("Quitters never win!")
            print()
            print()
            game_over()
            sys.exit(0)
        else:
            print("Typing is hard, yo!\n")

# Character table


def print_character_menu(pos1, char1, pos2, char2, pos3, char3):
    print("-" * 110)
    print("{:<10}|| {:<30}|| {:<30}|| {:<30}|".format(
        "Name:", (pos1 + char1.name), (pos2 + char2.name), (pos3 + char3.name)))
    print("{:<10}|| {:<30}|| {:<30}|| {:<30}|".format(
        "Health:", char1.health, char2.health, char3.health))
    print("{:<10}|| {:<30}|| {:<30}|| {:<30}|".format(
        "Punch:", char1.punch_power.title(), char2.punch_power.title(), char3.punch_power.title()))
    print("{:<10}|| {:<30}|| {:<30}|| {:<30}|".format(
        "Kick:", char1.kick_power.title(), char2.kick_power.title(), char3.kick_power.title()))
    print("{:<10}|| {:<30}|| {:<30}|| {:<30}|".format(
        "Defense:", char1.defense.title(), char2.defense.title(), char3.defense.title()))
    print("{:<10}|| {:<30}|| {:<30}|| {:<30}|".format(
        "Special:", char1.special_name, char2.special_name, char3.special_name))
    print("-" * 110)


# Character selection function
def player_selection():
    print_character_menu("1. ", character1, "2. ",
                         character2, "3. ", character3)
    print_character_menu("4. ", character4, "5. ",
                         character5, "6. ", character6)
    print_character_menu("7. ", character7, "8. ",
                         character8, "9. ", character9)

# Looping user input to choose character
    while True:
        character_choice = input("Who will it be? (1-9) ")
        if character_choice == "1":
            player = character1
            return player
        elif character_choice == "2":
            player = character2
            return player
        elif character_choice == "3":
            player = character3
            return player
        elif character_choice == "4":
            player = character4
            return player
        elif character_choice == "5":
            player = character5
            return player
        elif character_choice == "6":
            player = character6
            return player
        elif character_choice == "7":
            player = character7
            return player
        elif character_choice == "8":
            player = character8
            return player
        elif character_choice == "9":
            player = character9
            return player
        else:
            print("Typing is hard, yo!")

# Game Fight function


def fight():

    while opponent_list[0].health > 0 and player.health > 0:

        print()
        print("What do you want to do?")
        print("1. Kick")
        print("2. Punch")
        print("3. %s" % (player.special_name))
        print("4. Flee")
        print(">>> ",)
        user_input = input()
# Kick
        if user_input == "1":
            # Player attacks opponent
            player.kick(opponent_list[0])
            if opponent_list[0].is_alive() == False:
                print("%s is dead.\n" % (opponent_list[0].name))
                print("")
                victory()
                opponent_list.pop(0)
                # Day 2 refactor.  Added new fuction to fix while loop "slap in the face".
                if len(opponent_list) >= 1:
                    keep_playing()
                    break
                else:
                    ending_story()
                    time.sleep(5)
                    sys.exit(0)
# Punch
        elif user_input == "2":
            # Player attacks opponent
            player.punch(opponent_list[0])
            if opponent_list[0].is_alive() == False:
                print("%s is dead.\n" % (opponent_list[0].name))
                print("")
                victory()
                opponent_list.pop(0)
                if len(opponent_list) >= 1:
                    keep_playing()
                    break
                else:
                    ending_story()
                    time.sleep(5)
                    sys.exit(0)

# Special
        elif user_input == "3":
            # Player attacks opponent
            player.special(opponent_list[0])
            if opponent_list[0].is_alive() == False:
                print("%s is dead.\n" % (opponent_list[0].name))
                print("")
                victory()
                opponent_list.pop(0)
                if len(opponent_list) >= 1:
                    keep_playing()
                    break
                else:
                    ending_story()
                    time.sleep(5)
                    sys.exit(0)
# RUN AWAY!!!!
        elif user_input == "4":
            print("QUITTERS NEVER WIN!")
            time.sleep(5)
            sys.exit(0)
        else:
            print(
                "Your keyboard skills need some work! You missed your chance to attack!\n")
# Computer ATTACKS!
        if player.health > 0:
            # Opponent attacks player
            opponent_list[0].rand_attack(player)
            if player.is_alive() == False:
                print("%s is dead." % (player.name))
                print("")
                print("")
                fatality()
                print("Better luck next time, chump.")
                time.sleep(5)
                sys.exit(0)


# print title screen
title()
# pygame.mixer.music.play(-1)

time.sleep(2)
input("Press any key to continue\n \n \n")

choose()
player = player_selection()

# Make a character list and opponent list
character_list = [character1, character2, character3, character4,
                  character5, character6, character7, character8, character9]
opponent_list = []
# when user selects a character, it moves remaining characters to opponents list for battle
for character in character_list:
    if player != character:
        opponent_list.append(character)

print("You have choosen %s" % (player))
print()

story()
ready = input("\nAre you ready to fight? (y or n) ")
if ready == "y":
    print("\nGET READY!\n")
else:
    print("\nToo bad! Time to fight!\n")

print("\nYour first opponent is: %s" % (opponent_list[0]))
fight_text()
fight()
