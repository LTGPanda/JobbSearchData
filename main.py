import argparse
from functools import wraps
import json


db = open('JobbGettingData/test.json','r')

data = json.load(db)

for i in data['Jobb']:
    print(i)
 
# Closing file
db.close()




# need some json labbing first
#parser = argparse.ArgumentParser()
#parser.add_argument('-p', dest='PrintPoint', type=str, default=False, required=False, help="prints out some random data points")
#
#parser.add_argument('-a', dest='add', type=str, nargs='?', default=False, required=False, help="Adds item to database")
#
#parser.add_argument('-P', dest="printData", type=int, nargs='?', default=0, required=False, help="prints out database")
#
#arguments = parser.parse_args()
#db = open('BigDB.json', 'r')
#
#def run(f):
#    @wraps(f)
#    def wrapper(*args, **kwargs):
#        pif = open(arguments.FileSet, 'r')
#    return wrapper
#
#
#
#
#@run
#def failed():
#    print ("Något gick fel i formationen")
#
#failed()