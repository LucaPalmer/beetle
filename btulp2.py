#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 16:31:12 2021

@author: luca
"""
#result is the rolled dice

import random
from time import sleep

dice = (1, 2, 3, 4, 5, 6)

dice_order = {1: "Body", 2:"Head", 3: "Antennae", 4: "Eye", 5: "Mouth", 6: "Leg"}

player = []
dice_counter = 0

print(""""Welcome to Beetle! Here are the rules: The aim is to collect all the body parts of a beetle. A dice roll of 1 gives a beetle body, 2 gives a head, 3 gives an antenna, 4 gives an eye, 5 gives a mouth, and 6 gives a leg. 
          
The player must collect a beetle body before any other body parts can be added. 
\nThe player must collect a beetle head before any antennae, eyes or mouth can be added.
--------------------------  

Press Enter to Roll the Dice!
""")

def body():
    result = 1
    if result in dice_order:
        if result == 1:
            player.insert(0, dice_order[result])

def head():
    result = 2
    if result in dice_order:
        if result == 2 or result == 6:
            player.insert(1, dice_order[result])

def antennae():
    result = 3
    if result in dice_order:
        if result == 3:
            player.append(dice_order[result])

def eye():
    result = 4
    if result in dice_order:
        if result == 4:
            player.append(dice_order[result])
            
def mouth():
    result = 5
    if result in dice_order:
        if result == 5:
            player.append(dice_order[result])

def leg():
    result = 6
    if result == 6:
        if result in dice_order:
            player.append(dice_order[result])

def beetle():
    global dice_counter
    #global player
    
    input() 
    result = random.choice(dice)
    dice_counter += 1
    player.sort()
    rotation = {1: body, 2: head, 3: antennae, 4: eye, 5: mouth, 6: leg}
    
    if len(player) == 13:
        print("Beetle: ", player, "\n")
        print("Congratulations, you won!\n")
        sleep(0.5)
        print("Your final body part was:", dice_order[result], "\n")
        sleep(0.5)
        print("It took you", dice_counter, "dice rolls to finish the game!")
        sleep(1)
        return
    
    else:

        if result == 1:
           if dice_order[1] not in player: #1 body required
                rotation[1]()

    if result == 2:
       if dice_order[1] in player and dice_order[2] not in player:  #1 head required
            rotation[2]()
           
    if result == 3:#2 antennas required
       if dice_order[1 and 2] in player: 
           if player.count("Antennae") < 2:
               rotation[3]()

    if result == 4:
        if dice_order[1 and 2] in player: #2 eyes required
            if player.count("Eye") < 2:    
                rotation[4]()
    
    if result == 5: 
        if dice_order[1 and 2] in player and [5] not in player: #1 mouth required
            if player.count("Mouth") < 1:
                rotation[5]()
            
    if result == 6: #6 legs required
        if dice_order[1] in player:
            if player.count("Leg") < 6:
                rotation[6]()
                
    print("Beetle: ", player, "\n")
    print("\nDice: ", result, "| You gained: ", dice_order[result], "\n")
    input("Press Enter to Roll Again!")
    print("\n--------------------------\n")
    sleep(0.3)
    beetle()
    
beetle()
    