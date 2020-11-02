#!/usr/bin/env python3
import sqlite3
import os.path
import json
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "poke.db")

import random
def randno():
    r=[]
    while(len(r)<=20):
        z=random.randrange(1,252)
        if(z not in r): # and z not in a and z not in b):
            r.append(z)
    return r

def getPoke(num):
    with sqlite3.connect('backend/poke.db') as conn:
        c = conn.cursor()
        c.execute('''SELECT * FROM pokedex where Rank = ?''',[num])
        obj = list(dict.fromkeys(c.fetchall()))
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
    def to_list(self):
        lists =[self.rank,self.name,self.height,self.weight,self.hp,self.attack,self.defense,
                self.sattack,self.sdefense,self.speed,self.url]
        return lists


def getobjects():
    pokearray_json= []
    pokearray = []
    # x=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    for i in randno():
        tempobj = Pokedex(i)
        pokearray.append(tempobj)
        pokearray_json.append(tempobj.to_list())
    return pokearray,pokearray_json
