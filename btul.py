#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 16:31:12 2021

@author: luca
"""
import random

dice = (1, 2, 3, 4, 5, 6)

dice_order = {1: "body", 2:"head", 3: "antennae", 4: "eye", 5: "mouth", 6: "leg"}

player = []

def body():
    result = random.choice(dice)
    if result in dice_order:
        if result == 1:
            player.append(dice_order[result])
            print("Dice: ", result)
            print("Beetle: ", player)
        else:
            print("Dice: ", result)
            print("You didn't roll one, try again.")

body()

def head():
    result = random.choice(dice)
    if dice_order[1] in player:
        if result in dice_order:
            if result == (3, 4, 5):
                player.append(dice_order[result])
            print("Dice: ", result)
            print("Beetle: ", player)
        else:
            print("Dice: ", result)
            print("You didn't roll one, try again.")

head()