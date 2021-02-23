#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 16:31:12 2021

@author: luca
"""
import random

beetle = {1: "body", 2:"head", 3: "antennae", 4: "eye", 5: "mouth", 6: "leg"}

player = []

dice = (1, 2, 3, 4, 5, 6)

def roll():
    result = random.choice(dice)
    for i in beetle:
        if i == result:
            player.append(beetle[i])
            print(result)
            print("Beetle: ", player)  