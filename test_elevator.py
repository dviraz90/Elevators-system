'''
This module contains test for elevator module.

test cases:
1.for each elevator type:
    test can_serve() method.
    test is_available() method.
'''

import unittest 
from building import ELEVATOR_DEF_DICT
import elevator as e


class test_elevator(unittest.TestCase):
    
    def setUp(self):
        #create elevators types
        self.fast_elev = e.Elevator(ELEVATOR_DEF_DICT["FAST"])
        self.standard_elev = e.Elevator(ELEVATOR_DEF_DICT["STANDARD"])
        self.cargo_elev = e.Elevator(ELEVATOR_DEF_DICT["CARGO"])

    def tearDown(self):
        pass    
    #check if fast can serve
    def test_fast_can_serve(self):
        self.assertTrue(self.fast_elev.can_serve(11,5,0))
        self.assertFalse(self.fast_elev.can_serve(15, 0, 45))
        self.assertFalse(self.fast_elev.can_serve(4, 0, 0))
    #check if standard can serve
    def test_standard_can_serve(self):
        self.assertTrue(self.standard_elev.can_serve(5, 10, 45))
        self.assertFalse(self.standard_elev.can_serve(10, 16, 50))
        self.assertFalse(self.standard_elev.can_serve(7, 15, 45))
    #check if cargo can serve
    def test_cargo_can_serve(self):
        self.assertTrue(self.cargo_elev.can_serve(11, 0, 500))
        self.assertFalse(self.cargo_elev.can_serve(6, 0 ,500))
        self.assertFalse(self.cargo_elev.can_serve(7, 0, 1000))
        self.assertFalse(self.cargo_elev.can_serve(7, 5, 500))
    #check if fast is available
    def test_fast_is_available(self):
        self.assertTrue(self.fast_elev.is_available())
        self.assertFalse(self.fast_elev.is_available())
    #check if standard is available
    def test_standard_is_available(self):
        self.assertTrue(self.standard_elev.is_available())
        self.assertFalse(self.standard_elev.is_available())
    #check if cargo is available
    def test_cargo_is_available(self):
        self.assertTrue(self.cargo_elev.is_available())
        self.assertFalse(self.cargo_elev.is_available())


if __name__ == '__main__':
    unittest.main()
