#!/usr/bin/env python3
import sqlite3

conn = sqlite3.connect('poke.db')
c = conn.cursor()

def getPoke(num):
    c.execute('''SELECT * FROM dex where rank = ?''',[num])
    obj =list(dict.fromkeys(c.fetchall()))
    return obj[0]
