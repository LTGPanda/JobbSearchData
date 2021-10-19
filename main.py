import argparse
from functools import wraps
import json

parser = argparse.ArgumentParser()
parser.add_argument('-p', dest='PrintPoint', default=False, action="store_true", required=False, help="prints out some random data points")

parser.add_argument('-a', dest='add', default=False, action="store_true", required=False, help="Adds item to database")

parser.add_argument('-P', dest="PrintData", default=False, action="store_true", required=False, help="prints out database")

parser.add_argument('-m', dest="AddMeet", type=str, nargs='?', default=False, required=False, help="adds a meeting in a added item")

arguments = parser.parse_args()

def run(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        db = open('JobbDB.json','r+')
        data = json.load(db)

        if arguments.add:
            print("add true")
            AddData(data, db)
        if arguments.PrintPoint:
            print("point true")
            PrintPoint(data)
        if arguments.PrintData:
            print("Data true")
            PrintData(data)

        db.close()

    return wrapper


def AddData(Data, fil):
    test = {"Name": "cunty","Where": "Din pappa","Meets": "55","Awnser": True,"Gotten": False}
    #test = json.dumps(test)

    Data.update(test)
    fil.seek(1)
    json.dump(Data, fil)
    PrintData(Data)#need to do in array or not have array

def PrintPoint(Data):
    return

def PrintData(Data):
    for item in Data['Jobb']:
        print(item)



@run
def failed():
    print ("Något gick fel i formationen")

failed()