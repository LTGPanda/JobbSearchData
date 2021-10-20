import argparse
from functools import wraps
import json

parser = argparse.ArgumentParser()
parser.add_argument('-a', dest='add', default=False, action="store_true", required=False, help="Adds item to database")

parser.add_argument('-p', dest="PrintData", default=False, action="store_true", required=False, help="prints out database")

parser.add_argument('-s', dest="Svar", type=str, nargs='?', default=False, required=False, help="Flips awneser to true")

parser.add_argument('-m', dest="AddMeet", type=str, nargs='?', default=False, required=False, help="adds a meeting in a added item")

parser.add_argument('-Hype', dest="Goted", type=str, nargs='?', default=False, required=False, help="Fuck yeah doode homie finaly got a jobb")

parser.add_argument('-hlep', dest="Hlep", default=False, action="store_true", required=False, help="Hlep but by me :)")


arguments = parser.parse_args()

def run(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        db = open('JobbDB.json','r+')
        data = json.load(db)
        db.close()

        if arguments.add:
            AddData(data)
        if arguments.PrintData:
            print("lol xd")
            for item in data:
                print(item)
        if arguments.Svar:
            Svarad(data)
        if arguments.AddMeet:
            Meet(data)
        if arguments.Goted:
            Pog(data)
        if arguments.Hlep:
            print("[-a] add new item, [-p] prints out data, [-s Name] Flips awnser to true, [-m Name] Adds to Meet counter, [-Hype] yo Pog")
    return wrapper


def Meet(Data):
    for item in Data:
        if item['Name'] == arguments.AddMeet:
            item['Meets'] = int(item['Meets']) + 1
    Safe(Data)

def Svarad(Data):
    for item in Data:
        if item['Name'] == arguments.Svar:
            item['Awnser'] = True
    Safe(Data)

def AddData(Data):
    Namn = input("Namn : ")
    vad = input("vad : ")
    newItem = {"Name": Namn,"What": vad,"Meets": 0,"Awnser": False,"Gotten": False}
    Data.append(newItem)
    Safe(Data)

def Pog(Data):
    for item in Data:
        if item['Name'] == arguments.Goted:
            item['Gotten'] = True
    print("Hype dude u got this :) ")
    Safe(Data)

def Safe(Data):
    with open('JobbDB.json', 'w') as fil:
        json.dump(Data, fil, indent=4, separators=(',', ': '))


@run
def failed():
    print ("Något gick fel i formationen")

failed()