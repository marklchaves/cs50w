class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(2, 8)

print("\nPoint\n")

print(p.x)
print(p.y)

class Flight():
    def __init__(self, flt_no, capacity):
        self.flt_no = flt_no
        self.capacity = capacity
        self.availability = capacity
        self.passengers = []

    def add_passenger(self, new_pass):
        if not self.availability:
            print(f"\nFlight {self.flt_no} is full.\n")
            print(f"\nNo seat available for passenger {new_pass}.\n")
            return False
        self.passengers.append(new_pass)
        print(f"\nPassenger {new_pass} added to Flight {self.flt_no}.\n")
        self.availability -= 1
        return True
    
flight1 = Flight(1, 3)

passenger_queue = ["Chewbacca Chaves", "Hope Chaves", "Millie Chaves", "Bobby Chaves"]

for p in passenger_queue:
    flight1.add_passenger(p)

print(f"\nFlight {flight1.flt_no} has these passengers: {flight1.passengers}\n")
