#!/usr/bin/env python3
import sqlite3
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "poke.db")


def getPoke(num):
    with sqlite3.connect('backend/poke.db') as conn:
        c = conn.cursor()
        c.execute('''SELECT * FROM pokedex where Rank = ?''',[num])
        obj =list(dict.fromkeys(c.fetchall()))
    return obj[0]


class Pokedex():
    def __init__(self,num):
        obj = getPoke(num)
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
        self.url = '/static/img/'+obj[0]+'.png'

def getobjects():
    pokearray= []
    for i in range(1,20):
        tempobj = Pokedex(i)
        pokearray.append(tempobj)
    print(pokearray[0].url)
    return pokearray

getobjects()
