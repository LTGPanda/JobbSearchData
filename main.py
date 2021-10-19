import argparse
from functools import wraps
import json

parser = argparse.ArgumentParser()
parser.add_argument('-p', dest='PrintPoint', default=False, action="store_true", required=False, help="prints out some random data points")

parser.add_argument('-a', dest='add', default=False, action="store_true", required=False, help="Adds item to database")

parser.add_argument('-P', dest="PrintData", default=False, action="store_true", required=False, help="prints out database")

arguments = parser.parse_args()

def run(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        db = open('test.json','r')
        data = json.load(db)
        
        if arguments.add:
            print("add true")
            AddData(data)
        if arguments.PrintPoint:
            print("point true")
            PrintPoint(data)
        if arguments.PrintData:
            print("Data true")
            PrintData(data)

        db.close()

    return wrapper


def AddData(Data):
    return

def PrintPoint(Data):
    return

def PrintData(Data):
    return


@run
def failed():
    print ("Något gick fel i formationen")

failed()