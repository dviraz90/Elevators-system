'''
This module is the main module.
handles the api using flask.
starts the server and it contains one URL that gets the data from the user.
'''

from flask import Flask
from building import Building

#constant dictionary with amout of each elevator type
#can change its values or add types
ELEVATORS_TYPES = {"FAST": 3,
                   "STANDARD": 2,
                   "CARGO": 1}

#create a building object
#can change floor number
b = Building(13, ELEVATORS_TYPES)
app = Flask(__name__)

#HTTP GET
@app.route('/elevator/<int:floor>/<int:persons>/<int:cargo>')
def get_elevator(floor, persons, cargo):
   res = b.request_elevator(floor, persons, cargo)
   return res


if __name__ == '__main__':
   app.run(debug=True)
