import sqlite3
import time


def main():
    data = sqlite3.connect('E:/test.db')
    table = input('please give name of data base')
    table.replace('\n','')
    c = data.cursor()
    c.execute('SELECT * FROM {0}'.format(table))
    dataRet = c.fetchall()
    for item in dataRet:
        print(item)

main()