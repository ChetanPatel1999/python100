#setdefault():- Returns the value of the specified key. If the key does not exist: insert the 
# key, with the specified value  
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.setdefault("color", "red")
print(x)
print(car)