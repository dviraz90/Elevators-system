'''
This module contains the Building class that handles the elevators system in a given building.

Building class:
    __init__(floors, elevators_types): Initializes the amount of floors in the building 
            and the amount of each elevator type.
        params: 
            floors --> int
            elevators_types --> dictionary key=type, value=amount

    request_elevator(req_floor, req_persons, req_cargo): 
        handles the elevator request.

ELEVATOR_DEF_DICT:
    A const dictionary defines the elevator types,
    this dictionary passed to the Elevator constructor.
    that way we keep the solution extencable.
'''

from elevator_linked_list import LinkedList
from elevator import Elevator


# A const dictionary defines the elevator types
# can change its values or add types
ELEVATOR_DEF_DICT = {"FAST":{"type":"Fast","min_floor":10, "odd_floors_only":False, "max_persons":5, "max_cargo":0 },
                     "STANDARD": {"type": "Standard", "min_floor": 0, "odd_floors_only": False, "max_persons": 10, "max_cargo": 50},
                     "CARGO": {"type": "Cargo", "min_floor": 0, "odd_floors_only": True, "max_persons": 0, "max_cargo": 750}}

class Building:
    
    def __init__(self, floors, elevators_types):
        self.floors = floors
        self.elevators_types = elevators_types
        self.types_list = []
        if floors < 10:
            elevators_types["FAST"] = 0
        for type in elevators_types:
            #create linkedList foreach elevator type
            llist = LinkedList()
            for i in range(elevators_types[type]):
                llist.push(Elevator(ELEVATOR_DEF_DICT[type]))
            #create list of linkedLists
            self.types_list.append(llist)
            
    def request_elevator(self, req_floor, req_persons, req_cargo):
        '''
            This method handles the elevator request.
            returns: 
                message with information about the requested elevator.

            params: 
                req_floor --> int
                req_persons --> int
                req_cargo --> int
        '''
        if req_floor > self.floors: 
            return "requested floor doesn't exist."

        #set a flage to check if elevator can serve
        can_serve_flage = False

        for llist in self.types_list:
            curr = llist.head
            #check if linkedList isn't empty
            if curr is not None:
                curr_elev = curr.data

                if curr_elev.can_serve(req_floor, req_persons, req_cargo): 
                    can_serve_flage = True
                    free = curr_elev.is_available()
                    
                    if free == 0:
                        message = "{} elevator is serving.".format(curr_elev.type)
                        
                        if curr.next is not None:
                            # move the head to the end of the linkedList
                            head_ref = llist.move_to_end(curr)
                            llist.head = head_ref
                            curr = llist.head
                        return message

                    else:
                        message = "{} elevator is in use, will be available in {} seconds.".format(
                        curr_elev.type,  free)
                else:    
                    continue

        if not can_serve_flage:            
            message =  "Non elevator matches the current request."
        return message

