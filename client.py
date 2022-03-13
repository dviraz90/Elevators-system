
import requests as req
import random as rand
import time

# some integration tests
for i in range(5):
    floor = rand.randint(10, 13)
    persons = rand.randint(0, 5)
    cargo = rand.randint(0, 0)
    a = req.get(f"http://127.0.0.1:5000/elevator/{floor}/{persons}/{cargo}")
    print(a.text)
    time.sleep(1)
print()

for i in range(4):
    floor = rand.randint(0, 13)
    persons = rand.randint(0, 10)
    cargo = rand.randint(0, 50)
    b = req.get(f"http://127.0.0.1:5000/elevator/{floor}/{persons}/{cargo}")
    print(b.text)
    time.sleep(1)
print()

for i in range(4):
    floor = rand.randint(0, 13)
    persons = rand.randint(0, 0)
    cargo = rand.randint(0, 750)
    c = req.get(f"http://127.0.0.1:5000/elevator/{floor}/{persons}/{cargo}")
    print(c.text)
    time.sleep(1)
   
