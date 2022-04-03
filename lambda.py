people = [
  {"name": "Shafin", "house": "Katgor"},
  {"name": "Tahfim", "house": "2no gate"},
  {"name": "Ehan", "house": " Alif tower"}
  ]
  
def f(person):
  return person["name"]
people.sort(key = f)

print(people)

people = [
  {"name": "Shafin", "house": "Katgor"},
  {"name": "Tahfim", "house": "2no gate"},
  {"name": "Ehan", "house": " Alif tower"}
  ]
  
people.sort(key = lambda person: person["house"])

print(people)