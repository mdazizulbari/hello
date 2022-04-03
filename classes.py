class Point():
  def _init_(self, input1, input2):
    self.x = input1
    self.y = input2
    
p = point(2, 8)
print(p.x)
print(p.y)

class Flight():
  def _init_(self, capacity ):
    self.capacity = capacity
    self.passengers = []
  def add_passenger(self, name):
    if not self.open_seats():
      return False
    self.passenger.append(name)
    return True
  def open_seats(self):
    return self.capacity - len(self.passengers)
Flight = Flight(3)

people = ["Shafin", "Mahin", " Thafim", "Ehan"]
for person in people:
  if flight.add_passenger(person):
    print(f"Added {person} to flight successfully.")
  else:
    print(f"No available seats for {person}.")
