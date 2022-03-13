# Elevators System Management

## A management system for building elevators.

 <br>
<br>

# Project Description

## This is an API based app, for manageing the elevators timing system for a giver building.

## The user sends a HTTP GET request to the api's URL with the following parameters:
* #### requested floor number - int
* #### number of persons - int 
* #### cargo weight - int

## There are three types of elevators:
* #### <strong>Fast elevator</strong>  - work for 10th floor and up, max capacity 5 persons no cargo
* #### <strong>Standard elevator</strong> - work for all floors, max capacity 10 persons 50Kg cargo
* #### <strong>Cargo elevator</strong> - work for odd floors, max capacity no persons 750Kg cargo.

## The system provides the first elevator that matches the request. 
## For each request, the user gets a message with the status of the elevator:

* #### <strong>"{elevator_type} is serving"</strong> - if the elevator can serve the request and it's available
* #### "<strong>{elevator_type} elevator is in use, will be available in {seconds_num} seconds.</strong>" - if the elevator can serve the request but it's not available
* #### <strong>"Non elevator matches the current request."</strong> - if non of elevator can serve the request.

## Technologies:
#### In this project i used Flask for the server management - listening on port 5000.
#### URL's Example: localhost:5000/elevator/5/5/6, according the previous parameters.


### unit test - For testing the modules
<br>

## Architecture:
#### The architecture designed to be extencable.
#### The Elevator class a generic class for elevator.
<br>

#### It get its parameters in the constructor from the building module, were the ELEVATOR_DEF_DICT is, which defines the elevators types with their constraints.
<br>

#### The Building calss gets to its constructor a dictionary of elevators type and their amount,then it ctreates elevator objects, and sends constraints to their constructor. 
#### Also the Building constructor builds 3 linked lists for each elevator type.
<br>

#### The Building has the request_elevator method that takes the same parameters from the request and checks the availabilty of each elevator type.
#### It's starting with the Fast elevator linked list, if it matches the request it returns immediately the elevator type and moves the object to the end of the linked list.
#### Otherwise it moves to the next elevator typelinked list.
#### this solution gives an O(1) search.

## Usege
### start the server:
#### python server.py
<br>

### get request:
#### curl localhost:5000/elevator/5/5/6
<br>

### tests:
#### test_elevator.py - tests the elevator module

#### test_building.py - tests the building module

<br>

### notes:
#### you can change the call to Building by put other parameters.

#### I want to add a timing test in the future, right now i have a difficalt to mock time.