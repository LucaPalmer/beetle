#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 16:31:12 2021

@author: luca
"""
#result is the rolled dice

import random
import time
from time import sleep

start_time = time.time()

dice = (1, 2, 3, 4, 5, 6)

dice_order = {1: "Body", 2:"Head", 3: "Antennae", 4: "Eye", 5: "Mouth", 6: "Leg"}

player = ['Antennae',
 'Antennae',
 'Body',
 'Eye',
 'Eye',
 'Head',
 'Leg',
 'Leg',
 'Leg',
 'Leg',
 'Leg',
 'Leg',
 'Mouth']
player_2 = []

dice_counter = 0

print("""\nWelcome to Beetle! Here are the rules: The aim is to collect all the body parts of a beetle. A dice roll of 1 gives a beetle body, 2 gives a head, 3 gives an antenna, 4 gives an eye, 5 gives a mouth, and 6 gives a leg. 
          
The player must collect a beetle body before any other body parts can be added. 
\nThe player must collect a beetle head before any antennae, eyes or mouth can be added.
--------------------------  

Press Enter to Roll the Dice!
""")

input() 

def body():
    result = 1
    if result in dice_order:
        if result == 1:
            player.insert(0, dice_order[result])

def body_2():
    result = 1
    if result == 1:
        if result in dice_order:
            player_2.insert(0, dice_order[result])

def head():
    result = 2
    if result in dice_order:
        if result == 2 or result == 6:
            player.insert(1, dice_order[result])
            
def head_2():
    result = 2
    if result in dice_order:  
        if result == 2 or result == 6:
            player_2.insert(1, dice_order[result])

def antennae():
    result = 3
    if result in dice_order:
        if result == 3:
            player.append(dice_order[result])
            
def antennae_2():
    result = 3
    if result in dice_order:
        if result == 3:
            player_2.append(dice_order[result])

def eye():
    result = 4
    if result in dice_order:
        if result == 4:
            player.append(dice_order[result])

def eye_2():
    result = 4
    if result in dice_order:
        if result == 4:
            player_2.append(dice_order[result])
            
def mouth():
    result = 5
    if result in dice_order:
        if result == 5:
            player.append(dice_order[result])
            
def mouth_2():
    result = 5
    if result in dice_order:
        if result == 5:
            player_2.append(dice_order[result])

def leg():
    result = 6
    if result == 6:
        if result in dice_order:
            player.append(dice_order[result])

def leg_2():
    result = 6
    if result == 6:
        if result in dice_order:
            player_2.append(dice_order[result])


def beetle():        
    global dice_counter
        
    result = random.choice(dice)
    dice_counter += 1
    player.sort()
    rotation = {1: body, 2: head, 3: antennae, 4: eye, 5: mouth, 6: leg}
    
    """
    if len(player) == 13:
        end_time = time.time()
        print("Beetle: ", player, "\n")
        print("Congratulations, you won!\n")
        sleep(0.5)
        print("Your winning body part was:", dice_order[result], "\n")
        sleep(0.5)
        print("It took you", dice_counter, "dice rolls to finish the game!\n")
        sleep(0.5)
        print("Time Elapsed: ", round(end_time - start_time), "Seconds")
        sleep(1)
        return
    """
    #else:

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
    #sleep(0.7)
    beetle_2()
    
    
def beetle_2():
    global dice_counter
    
    result = random.choice(dice)
    dice_counter += 1
    player_2.sort()
    rotation = {1: body_2, 2: head_2, 3: antennae_2, 
                4: eye_2, 5: mouth_2, 6: leg_2}
        
    if len(player_2) == 13:
        end_time = time.time()
        print("Beetle (Player 2): ", player_2, "\n")
        print("Congratulations Player 2, you won!\n")
        sleep(0.5)
        print("Your winning body part was:", dice_order[result], "\n")
        sleep(0.5)
        print("It took you", dice_counter, "dice rolls to finish the game!\n")
        sleep(0.5)
        print("Time Elapsed: ", round(end_time - start_time), "Seconds")
        sleep(1)
        return
    
    if result == 1:
        if dice_order[1] in player:
            if dice_order[1] not in player_2:
                rotation[1]()

    if result == 2:
       if dice_order[1] in player and player_2:
           if dice_order[2] not in player_2:
               rotation[2]()
           
    if result == 3:
        if dice_order[1 and 2] in player:
            if dice_order [1 and 2] in player_2:
                if player_2.count("Antennae") < 2:
                    rotation[3]()

    if result == 4:
        if dice_order[1 and 2] in player:
            if dice_order[1 and 2] in player_2:
                if player_2.count("Eye") < 2:    
                    rotation[4]()
    
    if result == 5: 
        if dice_order[1 and 2] in player:
            if dice_order [2] in player_2: 
                if dice_order[5] not in player_2:
                    if player_2.count("Mouth") < 1:
                        rotation[5]()
            
    if result == 6:
        if dice_order[1] in player_2:
             if player_2.count("Leg") < 6:
                rotation[6]()
                
    print("Beetle 2: ", player_2, "\n")
    print("\nDice: ", result, "| You rolled: ", dice_order[result], "\n")
    print("Press Enter to Roll!")
    input("\n--------------------------\n")
    #sleep(0.4)
    
if len(player) == 13: 
    print("One more beetle to go!")
    while len(player) == 13:
        beetle_2()
        if len(player_2) == 13:
            break



beetle()
    