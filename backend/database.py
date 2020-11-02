#!/usr/bin/env python3
import sqlite3


def getPoke(num):
    conn = sqlite3.connect('poke.db',check_same_thread=False)
    c = conn.cursor()
    c.execute('''SELECT * FROM Pokedex where rank = ?''',[num])
    obj =list(dict.fromkeys(c.fetchall()))
    conn.close()
    return obj[0]
