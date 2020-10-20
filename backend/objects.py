#!/usr/bin/env python3
import database as db

class Pokedex():
    def __init__(self,num):
        obj = db.getPoke(num)
        self.rank = obj[0]
        self.name = obj[1]
        self.height = obj[2]
        self.weight = obj[3]
        self.hp = obj[4]
        self.attack = obj[5]
        self.defense = obj[6]
        self.sattack = obj[7]
        self.sdefense = obj[8]
        self.speed = obj[9]

