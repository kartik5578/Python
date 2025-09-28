data = {1:"karitk", 2:"Sakshi", 3:"Srushti", 4:"Atharva"}
print(data[2])
print(data.get(5, "Not found"))
print(data)

keys = [1, 2, 3, 4]
values = ["ram", "sham", "rohan", "rahul"]

newdata = dict(zip(keys, values))
print(newdata)

