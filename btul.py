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
    if result in dice_order:
        if result == 1:
            player.append(dice_order[result])
            print("Dice: ", result)
            print("Beetle: ", player)
        else:
            print("Dice: ", result)
            print("You didn't roll one, try again.")


def head():
    if dice_order[1] in player:
        if result in dice_order:
            if result == 2 or result == 6:
                player.append(dice_order[result])
            print("Dice: ", result)
            print("Beetle: ", player)
        else:
            print("Dice: ", result)
            print("You didn't roll two, try again.")

def head_features():
    if dice_order[1 and 2] in player:
        if result in dice_order:
            if result == 3 or result == 4 or result == 5 or result == 6:
                player.append(dice_order[result])
            print("Dice: ", result)
            print("Beetle: ", player)
        else:
            print("Dice: ", result)
            print("You didn't roll one, try again.")


def beetle():
   rotation = {1: body, 2: head, 3: head_features}
   
   