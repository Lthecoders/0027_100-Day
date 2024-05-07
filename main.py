import os
import random
import time

print("----------> Character Builder")
print("         ---------------------\n")
print("Please wait geating character builder ready.\n")
print("Loading...")

time.sleep(5)
os.system("clear")


def f_generater_character():
  character_name = input("Name your legend ---> ")
  first_dice = random.randrange(1, 6)
  second_dice = random.randrange(1, 12)
  print("\n", character_name, "\n")
  return (((first_dice * second_dice) / 2) + 10)


def f_character_strength():
  first_dice = random.randrange(1, 6)
  second_dice = random.randrange(1, 12)
  charater_health = (((first_dice * second_dice) / 2) + 12)
  print(" Strength -----> ", charater_health)


while True:
  # character_type={"Human","Elf","Wiard","Orc"}
  # print(character_type.pop())
  # f_generater_character()
  print("----------> Character Builder <-----------------\n\n")
  character_type = input("\nCharacter Type Human, Elf, Wizard, Orc ---->  ")
  print()
  health_player = f_generater_character()
  print(" HEALTH -----> ", health_player)
  print()
  f_character_strength()
  while True:
    NEXT_character = input(
        "\nDo you want to create a different charater ? (yes or no ONLY)----> "
    )
    if NEXT_character == "yes":
      os.system("clear")
      print(
          "\n\n\n -------> Saving your character's stats so you can access them later on.....\n"
      )
      print("Please wait....")
      time.sleep(6)
      os.system("clear")
      break
    if NEXT_character == "yes":
      os.system("clear")
      print(
          "\n Saving your character's stats so you can access them later on.....\n"
      )
      time.sleep(3)
      break
    elif NEXT_character == "no":
      print("\n\nMay your name go down in Legend....")
      exit()

    elif NEXT_character != "yes" and NEXT_character != "no":
      print(
          "\033[31m",
          "\n ALERT!!! you can only input yes or no in lowercase.<-------\n\n",
          "\033[0m")
      continue
