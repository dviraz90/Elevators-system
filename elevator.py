'''
This modul handles the Elevators definition.
Base class: 
    Elevator - represents a single elevator.

constructor:
    gets a dictionary with all elevator properties a constraints.
    each elevator object get its type by the constraints.

It has the following methods:
     reserve() - simulating the time of serving tenant request if available.
    is_available(): Check if the elevator is done serving (after 10 seconds of serving).
        returns: seconds left to serve.
    can_serve() : Check if the elevator can serve according to its constraints.
        returns : boolean
'''

from datetime import datetime,timedelta

class Elevator:

    def __init__(self, elev_type_params):
        self.min_floor = elev_type_params["min_floor"]
        self.odd_floors_only = elev_type_params["odd_floors_only"]
        self.max_persons = elev_type_params["max_persons"]
        self.max_cargo = elev_type_params["max_cargo"]
        self.type = elev_type_params["type"]
        self.when_free = datetime.now()
        self.SERVE_TIME = 10 # assumed constant time for elevator serve time.

    def _reserve(self):
        self.when_free = datetime.now() + timedelta(seconds=self.SERVE_TIME)

    def is_available(self):
        curr_time = datetime.now()
        if curr_time >= self.when_free:
            self._reserve()
            return 0
        return (self.when_free.second - curr_time.second)%60


    def can_serve(self, req_floor, req_persons, req_cargo):
        if (req_floor >= self.min_floor and 
            req_persons <= self.max_persons and 
            req_cargo <= self.max_cargo):
            #check for the ood floors
            if self.odd_floors_only:
                return req_floor%2 == 1

            return True

        return False
    








