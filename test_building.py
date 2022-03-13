'''
This module contains testfor building module.
tested on  2 different versions of buildings.

test cases:
1. foreach elevator type test:
    amount of elevator type test

2.floors validation
'''


import unittest
from building import Building
from unittest.mock import patch
import datetime



class test_building(unittest.TestCase):
   
    def setUp(self):
        #creat building instances:
        self.b1 = Building(14, {"FAST": 3, "STANDARD": 2,"CARGO": 1})
        self.b2 = Building(7, {"FAST": 3,"STANDARD": 3,"CARGO": 1})
    
   
    def call_elev(self):
        self.b1.request_elevator(12,5,0)
    
    def tearDown(self):
        pass

    #checks the amount of fast elevators in each building
    def test_fast_elevator_amount(self):
        #check for b1
        for i in range(self.b1.elevators_types["FAST"]):
            self.assertEqual("Fast elevator is serving.", self.b1.request_elevator(13,4,0))

        self.assertNotEqual("Fast elevator is serving.",self.b1.request_elevator(13, 4, 0))
        #check for b2
        for i in range(self.b2.elevators_types["FAST"]):
            self.assertNotEqual("Fast elevator is serving.", self.b2.request_elevator(3,4,0))

    #checks the amount of standard elevators in each building
    def test_standard_elevator_amount(self):
        #check for b1
        for i in range(self.b1.elevators_types["STANDARD"]):
            self.assertEqual("Standard elevator is serving.",self.b1.request_elevator(13, 4, 50))
        
        self.assertNotEqual("Standard elevator is serving.",self.b1.request_elevator(11, 2, 0))
        #check for b2
        for i in range(self.b2.elevators_types["STANDARD"]):
            self.assertEqual("Standard elevator is serving.",self.b2.request_elevator(3, 4, 50))
        
        self.assertNotEqual("Standard elevator is serving.",self.b2.request_elevator(6, 2, 0))

    #checks the amount of cargo elevators in each building
    def test_cargo_elevator_amount(self):
        #check for b1
        for i in range(self.b1.elevators_types["CARGO"]):
            self.assertEqual("Cargo elevator is serving.", self.b1.request_elevator(13, 0, 550))

        self.assertNotEqual("Cargo elevator is serving.",self.b1.request_elevator(3, 0, 150))
        #check for b2
        for i in range(self.b2.elevators_types["CARGO"]):
            self.assertEqual("Cargo elevator is serving.", self.b2.request_elevator(3, 0, 550))

        self.assertEqual("Cargo elevator is in use, will be available in 10 seconds.",self.b2.request_elevator(3, 0, 150))


    #checks if there is a valid amount of elevators in the request
    def test_request_valid_floors(self):
        #check for b1
        self.assertEqual("requested floor doesn't exist.", self.b1.request_elevator(20, 5, 2))
        #check for b2
        self.assertEqual("requested floor doesn't exist.", self.b2.request_elevator(10, 5, 2))

    
    
if __name__=="__main__":
    unittest.main()
