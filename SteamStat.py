import urllib.request
import sqlite3
import time

def main():
    gamezToWatch = {"PUBG":"http://steamcommunity.com/app/578080","SQUAD":"http://steamcommunity.com/app/393380","CSGO":"http://steamcommunity.com/app/730","TF2":"http://steamcommunity.com/app/440",
                    "RUST":"http://steamcommunity.com/app/252490","H1Z1":"http://steamcommunity.com/app/433850","RB6":"http://steamcommunity.com/app/359550"}
    data = sqlite3.connect('E:/test.db')
    for key,value in gamezToWatch.items():
        nb = retrieveCount(value)
        print("{0} players in {1}".format(nb,key))
        createTableForGame(data,key)
        addValueToTableOfGame(data,nb,key)
    data.close()


def addValueToTableOfGame(base,value,game):
    c = base.cursor()
    t= timestamp()
    c.execute("INSERT INTO {0} VALUES('{1}','{2}',{3})".format(game,t[0],t[1],value))
    c.close()

def createTableForGame(base,game):
    c= base.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS {0}(day TEXT, hourmin TEXT, numberofplayer REAL)".format(game))
    base.commit()
    c.close()


def timestamp():
    t = time.localtime()
    return (str(t.tm_year)+"-"+str(t.tm_mon)+"-"+str(t.tm_mday)," h"+str(t.tm_hour)+" m"+str(t.tm_min))


def retrieveCount(url):
    response = urllib.request.urlopen(url)
    htmlResp = response.read().decode('utf-8')
    startAt = htmlResp.find("apphub_NumInApp")
    if startAt == -1:
        print("nothing to be seen at {0}".format(url))
        return -1
    stopAt = htmlResp.find(" ",startAt)
    value = htmlResp[startAt:stopAt]
    value = value.split('>')[1]
    value = value.split(' ')[0]
    value = value.replace(',','')
    return value

for k in range(5):
    print("eh we go !")
    main()
    if k != 4:
        time.sleep(10)
