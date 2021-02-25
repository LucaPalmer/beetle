#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 16:31:12 2021

@author: luca
"""
#result is the rolled dice

import random

dice = (1, 2, 3, 4, 5, 6)

dice_order = {1: "body", 2:"head", 3: "antennae", 4: "eye", 5: "mouth", 6: "leg"}

player = []

def body():
    result = 1
    if result in dice_order:
        if result == 1:
            player.insert(0, dice_order[result])
        else:
            print("Dice: ", result)
            print("You didn't roll one, try again.")


def head():
    result = 2
    if result in dice_order:
        if result == 2 or result == 6:
            player.insert(1, dice_order[result])
        else:
            print("Dice: ", result)
            print("You didn't roll two, try again.")

def antennae():
    result = 3
    if result in dice_order:
        if result == 3:
            player.insert(2, dice_order[result])
        else:
            print("Dice: ", result)
            print("You didn't roll one, try again.")

def eye():
    result = 4
    if result in dice_order:
        if result == 4:
            player.insert(3, dice_order[result])
        else:
            print("Dice: ", result)
            print("You didn't roll one, try again.")
            
def mouth():
    result = 5
    if result in dice_order:
        if result == 5:
            player.insert(4, dice_order[result])
        else:
            print("Dice: ", result)
            print("You didn't roll one, try again.")

def leg():
    result = 6
    if result == 6:
        if result in dice_order:
            player.append(dice_order[result])
        else:
            print("Dice: ", result)
            print("You didn't roll one, try again.")

def beetle():
    result = 6
    rotation = {1: body, 2: head, 3: antennae, 4: eye, 5: mouth, 6: leg}
   
    if result == 1:
       if dice_order[1] not in player: #1 body required
           rotation[1]()

    if result == 2:
       if dice_order[2] not in player:  #1 head required
           rotation[2]()
   
    if result == 3:
       if dice_order[3] not in player: #2 antennas required
           rotation[3]()

    if result == 4:
        if dice_order[4] not in player: #2 eyes required
            rotation[4]()
    
    if result == 5: 
        if dice_order[5] not in player: #1 mouth required
            rotation[5]()
            
    if result == 6: #6 legs required
        if dice_order[6] not in player:
            if player.count("leg") < 6:
                rotation[6]()
    print("Dice: ", result)
    print("Beetle: ", player)

beetle()
   
   